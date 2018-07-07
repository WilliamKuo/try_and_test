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
#1
# all log here
#logging.basicConfig(level=logging.DEBUG, filename='test.log',\
#    format='[%(asctime)s][%(name)s][%(levelname)s]:%(message)s')

#2
# can store in different file
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('aaaaaaaaaaaaa.log')
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)



A = [1,2,3,4,5,6]
B = [1,2,3,4,5,6]
C = [1,2,3,4,5,6]
for i, j, k in [(x, y, z)\
    for x in A\
    for y in B\
    for z in C]:
    #logging.debug('{}{}{}'.format(i, j, k))
    logger.debug('{}{}{}'.format(i, j, k))
    #print '{}{}{}'.format(i, j, k)





