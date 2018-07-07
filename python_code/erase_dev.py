from sys import argv
from commands import getstatusoutput
import time


if len(argv) == 1:
    print "Please add device EX: python erase_dev.py bcde \n" 
    raise

for device_label in argv[1]:
    print "deal with /dev/sd" + device_label,
    try:
        cmd = "mkfs.xfs /dev/sd" + device_label
        ret, res = getstatusoutput(cmd)
        if ret != 0:
            raise
        time.sleep(1)
        cmd = "wipefs -a /dev/sd" + device_label
        ret, res = getstatusoutput(cmd)
        if ret != 0:
            raise
        print "success"
    except:
        print "fail"    







