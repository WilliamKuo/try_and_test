import socket

hostname = 'yahoo.com'
addr = socket.gethostbyname(hostname)

print 'The address of {} is {}'.format(hostname, addr)
