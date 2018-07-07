#!/usr/bin/env python
# William 
# 2018.6.4
# Design an application layer network protocol

import os
import logging
import socket
from sys import argv
from commands import getstatusoutput


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def run_cmd(cmd):
    # print 'cmd:[{}]'.format(cmd)
    ret, res = getstatusoutput(cmd)
    _eight_bit_mask = 0xff
    # sig = ret & _eight_bit_mask
    ret = ret >> 8 & _eight_bit_mask
    # print 'ret:[{}] res:[{}]\n'.format(ret, res)

    return ret, res


class NSSHProtocol():
    PORT = 12345
    H_MAGIC = 'NSSH'
    SIZE_MAGIC = len(H_MAGIC)
    SIZE_RET = 1
    SIZE_DATA_TYPE = 1  # 0: cmd 1: result
    SIZE_DATA_ALL = 1
    SIZE_DATA_LEN = 4  # max 9999 byte?
    SIZE_HEADER =\
        SIZE_MAGIC +\
        SIZE_RET +\
        SIZE_DATA_TYPE +\
        SIZE_DATA_ALL +\
        SIZE_DATA_LEN

    OFFSET_MAGIC = 0
    OFFSET_MAGIC_END = OFFSET_MAGIC + len(H_MAGIC)
    OFFSET_RET = OFFSET_MAGIC_END
    OFFSET_RET_END = OFFSET_RET + SIZE_RET
    OFFSET_DATA_TYPE = OFFSET_RET_END
    OFFSET_DATA_TYPE_END = OFFSET_DATA_TYPE + SIZE_DATA_TYPE
    OFFSET_DATA_ALL = OFFSET_DATA_TYPE_END
    OFFSET_DATA_ALL_END = OFFSET_DATA_ALL + SIZE_DATA_ALL
    OFFSET_DATA_LEN = OFFSET_DATA_ALL_END
    OFFSET_DATA_LEN_END = OFFSET_DATA_LEN + SIZE_DATA_LEN
    OFFSET_DATA_START = OFFSET_DATA_LEN_END

    RET_SUCCESS = '0'
    RET_FAIL = '1'
    TYPE_CMD = '0'
    TYPE_RESULT = '1'
    TYPE_PATH = '2'
    DATA_ALL_TRUE = '0'
    DATA_ALL_FALSE = '1'
    DATA_TYPE_LIST = [TYPE_CMD, TYPE_RESULT]
    NSSH_PDU = '{MAGIC}{RET}{TYPE}{ALL}{LEN}{DATA}'

    CMD_EXIT = 'EXIT'

    DIR_LOG_PATH = '/tmp'

    def __init__(self, host_ip=''):
        self.host_ip = host_ip
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_send = self.s.send
        self.socket_recv = self.s.recv
        self.socket_close = self.s.close
        self.data_buffer = ''
        self.role = 'SERVER'

        logging.basicConfig(
            filename='{}/nssh.log'.format(self.DIR_LOG_PATH),
            level=logging.DEBUG,
            format='[%(asctime)s %(levelname)4.4s] %(message)s',
            datefmt='%I:%M:%S'
        )
        self.log = logging

    def packet_compose(self, ret, data_type, all_data, data):
        pdu = self.NSSH_PDU.format(
            MAGIC=self.H_MAGIC,
            RET=ret,
            TYPE=data_type,
            ALL=all_data,
            LEN=str(len(data)).zfill(self.SIZE_DATA_LEN),
            DATA=data
            )

        return pdu

    def packet_send(self, ret, data_type, all_data, data):
        pdu = self.packet_compose(ret, data_type, all_data, data)
        self.log.debug('DEBUG_{}_SEND:[{}]'.format(self.role, pdu))
        self.socket_send(pdu)

    def packet_recv(self):
        packet_res = self.socket_recv(self.SIZE_HEADER)
        self.log.debug('DEBUG_{}_RECV:[{}]'.format(self.role, packet_res))
        if self.H_MAGIC != packet_res[
                self.OFFSET_MAGIC:self.OFFSET_MAGIC_END]:
            raise Exception('MAGIC error')

        # ret = packet_res[self.OFFSET_RET:self.OFFSET_RET_END]
        # data_type = packet_res[
        #     self.OFFSET_DATA_TYPE:self.OFFSET_DATA_TYPE_END]
        data_all = packet_res[self.OFFSET_DATA_ALL:self.OFFSET_DATA_ALL_END]
        data_len = packet_res[self.OFFSET_DATA_LEN:self.OFFSET_DATA_LEN_END]
        # self.log.debug('DEBUG_DATA:[{}]'.format(
        #     (ret, data_type, data_all, data_len)))
        get_size = int(data_len)
        if get_size == 0:
            return ''
        data = self.socket_recv(int(data_len))
        self.log.debug('DEBUG_{}_DATA:[{}]'.format(self.role, data))

        if data_all == self.DATA_ALL_FALSE:
            return data + self.packet_recv()
        else:
            return data

    def run_client(self):
        self.s.connect((self.host_ip, self.PORT))
        self.role = 'CLIENT_{}'.format(os.getpid())

        #
        terminal_title = self.host_ip + '@root:{path}$'
        path = '~/'
        while True:
            cmd = raw_input(terminal_title.format(path=path))
            if cmd in ['n', 'N', 'no', 'NO']:
                cmd = self.CMD_EXIT
            elif cmd == '':
                continue

            self.packet_send(
                self.RET_SUCCESS,
                self.TYPE_CMD,
                self.DATA_ALL_TRUE,
                cmd)

            if cmd == self.CMD_EXIT:
                break

            data = self.packet_recv()
            # this print data is for client interact
            print data

            if cmd.split()[0] == 'cd':
                self.packet_send(
                    self.RET_SUCCESS,
                    self.TYPE_CMD,
                    self.DATA_ALL_TRUE,
                    'pwd')
                data = self.packet_recv()
                path = data

        self.socket_close()

    def run_server(self):
        fork_pids = []
        self.s.bind((self.host_ip, self.PORT))
        self.s.listen(5)

        # TODO: a good way to end server not ctrl-c
        while True:
            # remove close pid
            fork_pids = [p for p in fork_pids if check_pid(p)]
            conn, addr = self.s.accept()
            self.socket_send = conn.send
            self.socket_recv = conn.recv
            self.socket_close = conn.close

            # fork to accept multi client
            newpid = os.fork()
            if newpid != 0:
                fork_pids.append(newpid)
                # print 'fork child pid:{}'.format(newpid)
                self.log.debug('FORK PID LIST: {}'.format(fork_pids))

            else:
                # communicate cmd
                while True:
                    try:
                        data = self.packet_recv()
                    except Exception:
                        break

                    try:
                        cmd = data
                        if cmd.split()[0] == 'cd':
                            os.chdir(cmd.split()[1])
                            cmd_ret, cmd_res = (0, '')
                        elif cmd == self.CMD_EXIT:
                            break  # add flag to close connect
                        else:
                            cmd_ret, cmd_res = run_cmd(cmd)
                    except Exception:
                        self.log.error('run cmd "{}" fail'.format(cmd))
                        # ret = 1
                        result = ''
                    else:
                        # ret = 0
                        result = cmd_res

                    try:
                        self.packet_send(
                            self.RET_SUCCESS,
                            self.TYPE_RESULT,
                            self.DATA_ALL_TRUE,
                            result)
                    except Exception:
                        self.log.error('SERVER SEND FAIL')

                self.socket_close()
                # TODO: let parent know update pid list


if __name__ == '__main__':
    if len(argv) != 2:
        raise Exception('INPUT VARS NUMBER FAIL')
    elif argv[1] in ['c', 'C', 'client']:
        host = '18.216.117.9'
        C = NSSHProtocol(host_ip=host)
        C.run_client()
    elif argv[1] in ['s', 'S', 'server']:
        S = NSSHProtocol()
        S.run_server()
    else:
        raise Exception('INPUT FAIL')


exit(0)
