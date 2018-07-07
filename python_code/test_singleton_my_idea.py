#!/usr/bin/env python
from commands import getstatusoutput
import subprocess
import re
import os
import sys
import math
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
    ret, res = getstatusoutput(cmd)
    _eight_bit_mask = 0xff
    #sig = ret & _eight_bit_mask
    ret = ret >> 8 & _eight_bit_mask
    #print 'ret:[{}] res:[{}]\n'.format(ret, res)

    return ret, res



class Singleton(object):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    _instance = None

    def __init__(cls, *args, **kwargs):
        if cls._instance is None:
            Singleton._instance = cls

        cls.test_var = 0

    def __call__(cls, *args, **kwargs):
        print 'call me maybe'
        return cls._instance

    def set_print(cls, val=0):
        print cls.test_var
        cls.test_var = val
        print cls.test_var

class MyClass(Singleton):
    """
    Example class.
    """

    pass

def main():
    m1 = MyClass()
    m2 = MyClass()

    m1().set_print(11)
    m2().set_print(22)
    print m1
    print m2
    print m1()
    print m2()
    print  m1() is m2()
    print  m1 is m2

print '+++++++++++++++++++++++++++++++'
main()
