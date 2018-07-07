from commands import getstatusoutput 
import time

import os 
import stat

def run_cmd(cmd):
    print cmd
    ret, res = getstatusoutput(cmd)
    return ret, res


def test():

    run_cmd('lvcreate -n LV_A -L 1G VG_A')
    mode = os.stat("/dev/VG_A/LV_A").st_mode
    print 'VG_A/LV_A ISBLK : {} '.format(stat.S_ISBLK(mode))
    run_cmd('lvcreate -n LV_B -L 1G VG_B')
    print 'VG_B/LV_B ISBLK : {} '.format(stat.S_ISBLK(mode))
    #time.sleep(1)
    ret, res = run_cmd('btier_setup -c -f /dev/VG_A/LV_A:/dev/VG_B/LV_B')
    print ret
    print res
    if ret != 0:
        raise
    #time.sleep(3)
    #run_cmd('make-bcache -B /dev/sdtierb')
    #time.sleep(2)
    #run_cmd('echo 1 > /sys/block/bcache0/bcache/stop')
    #time.sleep(2)
    #run_cmd('dd if=/dev/zero count=1 bs=1024 seek=4 of=/dev/sdtierb')
    time.sleep(3)
    run_cmd('btier_setup -d /dev/sdtierb')
    time.sleep(1)
    run_cmd('lvremove -f VG_A/LV_A VG_B/LV_B')

count = 0
while True:
    count += 1
    print '=============================count={}'.format(count)
    test()
    time.sleep(1)











