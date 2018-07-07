from commands import getstatusoutput
 
CMD = 'megacli -CfgDsply -aALL'

def run_cmd(cmd):
    print cmd
    ret, res = getstatusoutput(cmd)
    return ret, res

#ret, res = run_cmd(CMD)

ret, res = run_cmd('echo -e "o\\nn\\np\\n\\n\\n+100M\\n'\
    'n\\np\\n\\n\\n+100M\\n'\
    'n\\np\\n\\n\\n+100M\\n'\
    'n\\np\\n\\n\\n+100M\\nw\\n" | fdisk {0}'.format('/dev/sdb'))

