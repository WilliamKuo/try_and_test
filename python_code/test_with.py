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
import thread
import logging
import time
import datetime
import socket
import tempfile
from sys import argv
from commands import getstatusoutput


def run_cmd(cmd):
    #print 'cmd:[{}]'.format(cmd)
    ret, res = getstatusoutput('sudo '+cmd)
    _eight_bit_mask = 0xff
    #sig = ret & _eight_bit_mask
    ret = ret >> 8 & _eight_bit_mask
    #print 'ret:[{}] res:[{}]\n'.format(ret, res)

    return ret, res


class Test(object):
    def __init__(self):
        print 'test_init'

    def __enter__(self):
        print 'test_start'

    def __exit__(self, type, value, traceback):
        print 'test_close'

with Test():
    print 'inside'



