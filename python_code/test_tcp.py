from commands import getstatusoutput
import subprocess
import re
import uuid
import os
import copy
import csv
import pprint
import re
import struct
import traceback
import logging
import time
import datetime
import socket


#host = socket.gethostname()
host = '10.90.7.18'
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#raw_input()
#s.sendall(b'Hello, world')
send_size = 1024 * 1024 
f = open('a', 'rb')
l = f.read(send_size)
while l:
    s.send(l)
    s.send(b'I send {}'.format(send_size))
    raw_input()
    l = f.read(send_size)
    #s.close()

    data = s.recv(20)
    print 'I get "{}"'.format(data)

#data = s.recv(1024)
s.close()
print('Received', repr(data))





