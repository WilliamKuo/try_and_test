import socket, sys 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060
port = sys.argv[1] 
while True:
    s.sendto('0', ('0.0.0.0', int(port)))
