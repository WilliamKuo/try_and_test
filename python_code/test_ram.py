from commands import getstatusoutput
import time
 
TEST_PATH = "/FS/TEST"

def run_cmd(cmd):
    print cmd
    ret, res = getstatusoutput(cmd)
    return ret, res

i = 0

while True:
    #i+=1
    localtime = time.asctime( time.localtime(time.time()) )
    try:
        ret, res = run_cmd('free -h')
        if ret == 0:
            DATA = "[{}]\n {}\n".format(localtime, res)
        else:
            DATA = "[{}] XXXXXXXXXXXXX".format(localtime)
        run_cmd('echo "{}" >> {}/{}'.format(DATA, TEST_PATH, 'RAM_DATA'))
    except:
        print "FAIL to echo \n"
    #finally:
    time.sleep(60)
        #print i






