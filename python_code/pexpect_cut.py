import pexpect

CMD = 'megacli -AdpAlILog -a0 -NoLog -Page 32'


child = pexpect.spawn(CMD)
child.expect ('Press <ENTER> to continue...')
print child.before
child.kill(0)


