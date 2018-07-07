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


A = [1,2,3,4,5,6]
B = [1,2,3,4,5,6]
C = [1,2,3,4,5,6]
#for i, j, k in [(x, y, z)\
#    for x in A\
#    for y in B\
#    for z in C]:
#    print '{}{}{}'.format(i, j, k)

for i, j, k in ((x, y, z)\
    for x in A\
    for y in B\
    for z in C):
    print 'A{} B{} C{}'.format(i, j, k)


#print ((x, y, z) for x in A for y in B for z in C)
#print [(x, y, z) for x in A for y in B for z in C]



