from commands import getstatusoutput

cmd = "smartctl -H /dev/sda"
ret, res = getstatusoutput(cmd)
print ret
print res

