#!/usr/bin/env python
###############################################################################
#  (C) Copyright Promise Technology Inc., 2014 All Rights Reserved            #
#  Author: William Kuo <william.kuo@tw.promise.com>                           #
#  Date: 2017-02-14                                                           #
#  Reference:                                                                 #
#     https://www.ietf.org/rfc/rfc1035.txt                                    #  
#     https://www.youtube.com/watch?v=HdrPWGZ3NRo                             #  
#  DNS:                                                                       #  
#                                                                             #  
#                                                                             #  
###############################################################################

import socket
import struct


def _hex_1_byte_2_int(byte_str):
    ret = struct.unpack('B', byte_str)[0]

    # int number
    return ret


def _int_2_1_byte_hex(nu):
    list_hex = ['a', 'b', 'c', 'd', 'e', 'f']
    up = nu >> 4
    if up >= 10:
        up = list_hex[up - 10]
    down = nu & 0x0f
    if down >= 10:
        down = list_hex[down - 10]
    
    int_str = '{}{}'.format(up, down)
    ret = int_str.decode('hex')

    # 1 byte hex str
    return ret


def _get_flags(err=False):
    QR = 1<<7                               # this flag means response
    OPCODE = 0<<6 | 0<<5 | 0<<4 | 0<<3      # specifies kind of query in this message(4bit)
    AA = 1<<2                               # Authoritative Answer
    TC = 0<<1                               # TrunCation
    RD = 0<<0                               # Recursion Desired
    RA = 0<<7                               # Recursion Available
    Z = 0<<6 | 0<<5 | 0<<4                  # Reserved for future use(3bit)  
    #RCODE =  0<<3 | 0<<2 | 0<<1 | 0<<0     # Response code(4bit)
    if err:
        RCODE =  0<<3 | 0<<2 | 1<<1 | 1<<0  # Response code(4bit)
    else:
        RCODE =  0<<3 | 0<<2 | 0<<1 | 0<<0  # Response code(4bit)
    # flag is revert?
    return _int_2_1_byte_hex(QR | OPCODE | AA | TC | RD) +\
         _int_2_1_byte_hex(RA | Z | RCODE)    


def _get_question_domain(data):
    state = 0
    excepected_length = 0
    domain_str = ''
    domain_parts = list()
    str_end = 0
    final_end = 0

    for byte in data:
        if state == 1:
            domain_str += byte
            str_end += 1
            # end string byte
            if byte == '\x00':
                break
            elif str_end >= excepected_length:
                domain_parts.append(domain_str)
                domain_str = ''
                state = 0
                str_end = 0
        else:
            state = 1
            # First Byte store string length
            excepected_length = struct.unpack('B', byte)[0]
        
        final_end += 1

    question_type = data[final_end] + data[final_end+1]

    return domain_parts, question_type


def _build_responese(data, IP, error=False):
    ################# HEADER ##################################################
    TID = data[:2]             # Transaction ID
    Flags = _get_flags(error)  # Flags (QR|Opcode|AA|TC|RD|RA|Z|RCODE)
    QDCOUNT = '\x00\x01'       # Question count
    ANCOINT = '\x00\x01'       # Answer count
    NSCOUNT = '\x00\x00'       # Name server count
    ARCOUNT = '\x00\x00'       # Additional count

    dns_header = TID + Flags + QDCOUNT + ANCOINT + NSCOUNT + ARCOUNT

    ################# QUESTION SECTION ########################################
    domain, question_type = _get_question_domain(data[12:])

    QNAME = ''                 # domain name
    for part in domain:
        length = int(len(part))
        QNAME += _int_2_1_byte_hex(length)
        for char in part:
            QNAME += _int_2_1_byte_hex(int(ord(char)))
    # End QNAME byte
    QNAME += '\x00'

    QTYPE = question_type      # type of the query
    QCLASS = '\x00\x01'        # class of the query
    
    dns_question = QNAME + QTYPE + QCLASS 

    ################# RESOURCE RECORD #########################################
    NAME = '\xc0\x0c'          # resource record pertains domain name
    TYPE = '\x00\x01'          # RR type codes
    CLASS = '\x00\x01'         # class of the data in RDATA 
    TTL = '\x00\x00\x00\x00'   # interval (in seconds) resource record cached
    RDLENGTH = '\x00\x04'      # RDATA field length
    RDATA = ''                 # RDATA field Internet address
    for byte in IP.split('.'):
        byte = _int_2_1_byte_hex(int(byte))
        RDATA += byte

    dns_body = NAME + TYPE + CLASS + TTL + RDLENGTH + RDATA

    # Ready to sent
    return dns_header + dns_question + dns_body


###############################################################################
#                                 MAIN                                        #
###############################################################################

tmp_ptr_ip = ''
our_domain = ['vstor','com']
server_address = '10.90.7.12' # Service IP
port = 53              # DNS PORT
# "socket.AF_INET" is IPv4 "socket.SOCK_DGRAM" is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((server_address, port))

while True:
    # Wait and get request
    data, cli_address = s.recvfrom(512) # UDP is less equal than 512 bytes
    
    # Match
    domain, question_type = _get_question_domain(data[12:])
    match = True
    i = 0
    for part in domain:
        if i >= len(our_domain):
            break
        elif our_domain[i] != part:
            match = False
            break
        i += 1

    # Response data 
    if match:
        response_data = _build_responese(data, IP='10.90.6.120', error=False)
        tmp_ptr_ip = '10.90.6.120'
    elif 'in-addr' in domain and 'arpa' in domain:
        #Forward-confirmed reverse DNS ?
        response_data = _build_responese(data, IP=tmp_ptr_ip, error=False)
    else:
        response_data = _build_responese(data, IP='0.0.0.0', error=True)

    # Send back
    s.sendto(response_data, cli_address)

















