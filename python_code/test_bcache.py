from commands import getstatusoutput 
import time

import os 
import stat

def run_cmd(cmd):
    print cmd
    ret, res = getstatusoutput(cmd)
    return ret, res


def test():

    run_cmd('lvcreate -n LV -L 1G VG')
    #time.sleep(3)
    ret, res = run_cmd('make-bcache -C /dev/VG/LV --wipe-bcache')
    print ret
    print res
    if ret != 0:
        raise

    ret, cset = run_cmd("bcache-super-show /dev/VG/LV |grep cset |awk '{print $2}'")


    while True: 
        run_cmd('echo 1 > /sys/fs/bcache/{}/stop'.format(cset))
        ret, res = run_cmd('ls /sys/fs/bcache')
        if cset not in res:
            break
        else:
            print sleep
            time.sleep(1)


    time.sleep(2)
    run_cmd('dd if=/dev/aero count=4 bs=1024 seek=4 of=/dev/VG/LV conv=fdatasync')
    time.sleep(1)
    run_cmd('lvremove -f VG/LV')

count = 0
while True:
    count += 1
    print '=============================count={}'.format(count)
    test()
    time.sleep(1)











