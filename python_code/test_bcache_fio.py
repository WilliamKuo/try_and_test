from commands import getstatusoutput
import time
 
TIMES = 25

#RW = 'read'
#RW = 'write'
#RW = 'randread'
#RW = 'randwrite'

def run_cmd(cmd):
    print cmd
    ret, res = getstatusoutput(cmd)
    return ret, res

def test_fio(RW):

    run_cmd('echo "" > /mnt/test/ff')
    time.sleep(1)
    fp = open("./FIO", 'a+')

    ret, res = run_cmd('fio --direct=1 --iodepth=32 --ioengine=libaio --blocksize=4k --rw={} --group_reporting --refill_buffers --name=target --size=4mb --filename=/mnt/test/ff'.format(RW))

    _fio_sys = '0.00'
    _fio_usr = '0.00'
    _fio_read = '0'
    _fio_write = '0'


    for line in res.split('\n'):
        if "read" in line and "iops" in line:
            _fio_read = int(line.split(",")[2][6:])
        if "write" in line and "iops" in line:
            _fio_write = int(line.split(",")[2][6:])
        if "cpu" in line:
            _fio_sys = line.split(",")[1][5:-1]
            #_fio_usr = line.split(",")[0][21:-1]

    if RW in 'randread':
        print _fio_read
        print _fio_sys
        fp.write("{}:{}\n".format(_fio_read, _fio_sys))
    if RW in 'randwrite':
        print _fio_write
        print _fio_sys
        fp.write("{}:{}\n".format(_fio_write, _fio_sys))

    fp.close()



def test(RW):

    run_cmd('echo "" > ./FIO')
    count = 0
    while True:
        count += 1
        #print '=============================count={}'.format(count)
        test_fio(RW)
        if count > TIMES:
            break
        time.sleep(1)

    fp = open("./FIO", 'r')
    res = fp.readlines()
    total = 0
    count = 0
    total_cpu = 0
    for line in res:
        if len(line) <= 1:
            continue
        total += int(line.split(':')[0])
        total_cpu += float(line.split(':')[1])
        count += 1
    print "============================="
    print "{}".format(RW)
    print "RESULT_IOPS: {}".format(total / count)
    print "RESULT_CPU: {}".format(total_cpu / float(count))
    print "============================="
    
    fpr = open("./RESULT", 'a+')
    fpr.write("=============================\n")
    fpr.write("{}\n".format(RW))
    fpr.write("RESULT_IOPS: {}\n".format(total / count))
    fpr.write("RESULT_CPU: {}\n".format(total_cpu / float(count)))
    fpr.write("=============================\n")
    fpr.close()
    
    fp.close()

run_cmd('echo "" > ./RESULT')

#LV
print '=============================================================='
print 'LV'
print '=============================================================='
run_cmd('lvcreate -n LV -l100%FREE VG')
time.sleep(1)
run_cmd('mkfs.xfs /dev/VG/LV')
time.sleep(1)
run_cmd('mount /dev/VG/LV /mnt/test/')
time.sleep(1)
fpr = open("./RESULT", 'a+')
fpr.write("LV\n")
fpr.close()
for RW in 'read', 'write', 'randread', 'randwrite':
    test(RW)
time.sleep(1)
run_cmd('umount /mnt/test')
time.sleep(1)
run_cmd('lvremove -y -f VG/LV')
time.sleep(1)

#LV + bcache 
print '=============================================================='
print 'LV+bcache'
print '=============================================================='
run_cmd('lvcreate -n LV -l100%FREE VG')
time.sleep(1)
run_cmd('make-bcache -B /dev/VG/LV')
time.sleep(1)
run_cmd('mkfs.xfs /dev/bcache0')
time.sleep(1)
run_cmd('mount /dev/bcache0 /mnt/test/')
time.sleep(1)
fpr = open("./RESULT", 'a+')
fpr.write("LV+bcache\n")
fpr.close()
for RW in 'read', 'write', 'randread', 'randwrite':
    test(RW)
time.sleep(1)
run_cmd('umount /mnt/test')
time.sleep(1)
run_cmd('echo 1 > /sys/block/bcache0/bcache/stop')
time.sleep(2)
run_cmd('dd if=/dev/zero count=1 bs=1024 seek=4 of=/dev/VG/LV')
time.sleep(2)
run_cmd('lvremove -y -f VG/LV')
time.sleep(1)

#LV + bcache + SSD + WT 
print '=============================================================='
print 'LV+bcache+SSD+WT'
print '=============================================================='
run_cmd('lvcreate -n LV -l100%FREE VG')
time.sleep(1)
run_cmd('make-bcache -B /dev/VG/LV')
time.sleep(1)
run_cmd('echo 08bcc343-0833-4850-9cab-634c9c7fde3e > /sys/block/bcache0/bcache/attach')
time.sleep(1)
run_cmd('echo 10m > /sys/block/bcache0/bcache/sequential_cutoff')
time.sleep(1)
run_cmd('mkfs.xfs /dev/bcache0')
time.sleep(1)
run_cmd('mount /dev/bcache0 /mnt/test/')
time.sleep(1)
fpr = open("./RESULT", 'a+')
fpr.write("LV+bcache+SSD+WT\n")
fpr.close()
for RW in 'read', 'write', 'randread', 'randwrite':
    test(RW)
time.sleep(1)
run_cmd('umount /mnt/test')
time.sleep(1)
run_cmd('echo 1 > /sys/block/bcache0/bcache/detach')
time.sleep(1)
run_cmd('echo 1 > /sys/block/bcache0/bcache/stop')
time.sleep(2)
run_cmd('dd if=/dev/zero count=1 bs=1024 seek=4 of=/dev/VG/LV')
time.sleep(2)
run_cmd('lvremove -y -f VG/LV')
time.sleep(1)

#LV + bcache + SSD + WA 
print '=============================================================='
print 'LV+bcache+SSD+WA'
print '=============================================================='
run_cmd('lvcreate -n LV -l100%FREE VG')
time.sleep(1)
run_cmd('make-bcache -B /dev/VG/LV')
time.sleep(1)
run_cmd('echo 08bcc343-0833-4850-9cab-634c9c7fde3e > /sys/block/bcache0/bcache/attach')
time.sleep(1)
run_cmd('echo writearound > /sys/block/bcache0/bcache/cache_mode')
time.sleep(1)
run_cmd('echo 10m > /sys/block/bcache0/bcache/sequential_cutoff')
time.sleep(1)
run_cmd('mkfs.xfs /dev/bcache0')
time.sleep(1)
run_cmd('mount /dev/bcache0 /mnt/test/')
time.sleep(1)
fpr = open("./RESULT", 'a+')
fpr.write("LV+bcache+SSD+WA\n")
fpr.close()
for RW in 'read', 'write', 'randread', 'randwrite':
    test(RW)
time.sleep(1)
run_cmd('umount /mnt/test')
time.sleep(1)
run_cmd('echo 1 > /sys/block/bcache0/bcache/detach')
time.sleep(1)
run_cmd('echo 1 > /sys/block/bcache0/bcache/stop')
time.sleep(2)
run_cmd('dd if=/dev/zero count=1 bs=1024 seek=4 of=/dev/VG/LV')
time.sleep(2)
run_cmd('lvremove -y -f VG/LV')
time.sleep(1)






