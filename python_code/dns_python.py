#!/usr/bin/env python
import socket
import dns.flags
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.resolver

import pprint

i = 0
IP = ['10.90.6.120', '10.90.6.121', '10.90.6.122', '10.90.6.123']


address = '10.90.7.12' # Service IP
port = 53 # DNS PORT
# socket.AF_INET  is IPv4
# socket.SOCK_DGRAM is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((address, port))
print 'AAAAAAAAAAAAAAA'

while True:
    (wire, address) = s.recvfrom(512) # UDP is less equal than 512 bytes
    notify = dns.message.from_wire(wire)
   
    # dns rr standfor resource record
    print 'notify========================================='
    #print 'additional      {}'.format(notify.additional)
    print 'answer          {}'.format(notify.answer)
    #print 'authority       {}'.format(notify.authority)
    #print 'edns            {}'.format(notify.edns)
    #print 'ednsflags       {}'.format(notify.ednsflags)
    #print 'first           {}'.format(notify.first)
    print 'flags           {}'.format(notify.flags)
    #print 'fudge           {}'.format(notify.fudge)
    #print 'had_tsig        {}'.format(notify.had_tsig)
    #print 'id              {}'.format(notify.id)
    print 'index           {}'.format(notify.index)
    #print 'keyalgorithm    {}'.format(notify.keyalgorithm)
    #print 'keyname         {}'.format(notify.keyname)
    #print 'keyring         {}'.format(notify.keyring)
    #print 'mac             {}'.format(notify.mac)
    #print 'multi           {}'.format(notify.multi)
    #print 'options         {}'.format(notify.options)
    #print 'origin          {}'.format(notify.origin)
    #print 'original_id     {}'.format(notify.original_id)
    #print 'other_data      {}'.format(notify.other_data)
    #print 'payload         {}'.format(notify.payload)
    print 'question        {}'.format(notify.question)
    #print 'request_mac     {}'.format(notify.request_mac)
    #print 'request_payload {}'.format(notify.request_payload)
    #print 'tsig_ctx        {}'.format(notify.tsig_ctx)
    #print 'tsig_error      {}'.format(notify.tsig_error)
    #print 'xfr             {}'.format(notify.xfr)
    print '==============================================='
    #print notify.question[0].name    


    #_address = '10.90.7.12'
    #_port = 1060
    #s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s2.bind((_address, _port))
    #s2.sendto(wire, ('8.8.8.8', 53))
    #while True:
    #    (_wire, _address) = s2.recvfrom(512)
    #    response = dns.message.from_wire(_wire)
    #    break
    #print type(response.answer[0].items[0])

    response = dns.message.make_response(notify)
    response.flags |= dns.flags.AA
    response.answer = response.question
    

    print 'response======================================='
    #print 'additional      {}'.format(response.additional)
    print 'answer          {}'.format(response.answer)
    #print 'authority       {}'.format(response.authority)
    #print 'edns            {}'.format(response.edns)
    #print 'ednsflags       {}'.format(response.ednsflags)
    #print 'first           {}'.format(response.first)
    print 'flags           {}'.format(response.flags)
    #print 'fudge           {}'.format(response.fudge)
    #print 'had_tsig        {}'.format(response.had_tsig)
    #print 'id              {}'.format(response.id)
    print 'index           {}'.format(response.index)
    #print 'keyalgorithm    {}'.format(response.keyalgorithm)
    #print 'keyname         {}'.format(response.keyname)
    #print 'keyring         {}'.format(response.keyring)
    #print 'mac             {}'.format(response.mac)
    #print 'multi           {}'.format(response.multi)
    #print 'options         {}'.format(response.options)
    #print 'origin          {}'.format(response.origin)
    #print 'original_id     {}'.format(response.original_id)
    #print 'other_data      {}'.format(response.other_data)
    #print 'payload         {}'.format(response.payload)
    print 'question        {}'.format(response.question)
    #print 'request_mac     {}'.format(response.request_mac)
    #print 'request_payload {}'.format(response.request_payload)
    #print 'tsig_ctx        {}'.format(response.tsig_ctx)
    #print 'tsig_error      {}'.format(response.tsig_error)
    #print 'xfr             {}'.format(response.xfr)
    #print '==============================================='
    print '\n\n\n\n\n\n\n'
    #print '==============================================='
    #print response.answer[0].to_text()
    #print response.answer[0].to_rdataset()
    #print response.answer[0].name
    #print response.answer[0].items
    #response.answer[0].remove(response.answer[0].items[0])
    #print type(response.answer[0].items[0])
    #print response.answer[0].items[0].address
    #print response.answer[0].items[0].covers
    #print response.answer[0].items[0].rdclass
    #print response.answer[0].items[0].rdtype

    #dns.rdata.Rdata.from_text()
    try:
        print '==============================================='
        rdata = dns.rdata.from_text(dns.rdataclass.IN, dns.rdatatype.A, IP[i])
        response.answer[0].add(rdata)
        #response.answer[0].items[0].address = '8.8.8.8'
        #response.answer[0].items[0].address = IP[i]
        print response.answer[0].items
        print response.answer[0].items[0].address
        i += 1
        if i >3:
            i = 0
    except:
        pass

    wire = response.to_wire(response)
    s.sendto(wire, address)




