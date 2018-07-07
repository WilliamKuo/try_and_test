from commands import getstatusoutput
import time
import uuid
 
TEST_PATH = "/mnt/vstor"

def run_cmd(cmd):
    print cmd
    ret, res = getstatusoutput(cmd)
    return ret, res


#normal touch file
i = 0
LABEL = str(uuid.uuid4())
while True:
    i+=1
    localtime = time.asctime( time.localtime(time.time()) )
    DATA = "[{}] {}".format(localtime, i)
    try:
        run_cmd('echo {} >> {}/{}'.format(DATA,TEST_PATH,'STRESS_TEST{}'.format(LABEL)))
    except:
        time.sleep(1)
        print "FAIL to echo \n"
    finally:
        print i
        #time.sleep(1)

# normal cp file rm file
#i = 0
#file_name = "100M"
#while True:
#    i+=1
#    try:
#        run_cmd('cp {} {}/{}7'.format(file_name,TEST_PATH,file_name))
#        time.sleep(1)
#        run_cmd('rm {}/{}7'.format(TEST_PATH,file_name))
#    except:
#        print "FAIL to cp or rm \n"
#    finally:
#        print i
#        #time.sleep(1)
#



##FTP
#i = 8
#import ftplib
#try:
#    session = ftplib.FTP('10.90.6.95')
#    print session.login('user{}'.format(i),'password{}'.format(i))
#    session.cwd("TEST")
#    session.set_pasv(False)
#    #session.retrlines('LIST')
#    while True:
#        localtime = time.asctime( time.localtime(time.time()) )
#        DATA = "[{}]".format(localtime)
#        run_cmd('echo {} > FTP_STRESS_TEST{}'.format(DATA, i))
#        file = open('FTP_STRESS_TEST{}'.format(i),'r') # file to send
#        try:
#            session.storlines('APPE FTP_STRESS_TEST{}'.format(i), file)     # send the file
#        except Exception as e:
#            print e
#        file.close()                                    # close file and FTP
#except Exception as e:
#    print e
#finally:
#    session.quit()
#
#





# SMB
#
#from smb.SMBConnection import SMBConnection
#
#userID = 'user1'
#password = 'password1'
#client_machine_name = 'DELL'
#
#server_name = 'vstor'
#server_ip = '10.90.6.95'
#
#domain_name = 'domainname'
#
#conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
#
#conn.connect(server_ip, 139)
#
#shares = conn.listShares()
#
#run_cmd('echo {} > SMB_STRESS_TEST{}'.format('TEST', '1'))
#time.sleep(1)
#with open('SMB_STRESS_TEST{}'.format(1),'r') as test_file: # file to send
#    conn.storeFile('TEST', 'SMB_STRESS_TEST{}'.format(1), test_file)
##test_file.close()
#
##for share in shares:
##    if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
##        sharedfiles = conn.listPath(share.name, '/')
##        for sharedfile in sharedfiles:
##            print(sharedfile.filename)
#
#conn.close()
