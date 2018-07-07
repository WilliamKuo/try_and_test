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


class counted(object):
    """ counts how often a function is called """
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)


@counted
def something():
    pass

something()
something()
something()
print something.counter



def cc():
    print 'call back'

def dd(call_bk=None):
    def real(function):
        def wrapper(*args, **kwargs):
            call_bk()

            return function(*args, **kwargs)

        return wrapper

    return real

@dd(cc)
def double(x):
    return x * 2 

print double(2)








