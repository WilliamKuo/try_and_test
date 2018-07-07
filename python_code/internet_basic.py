#! /usr/bin/env python

def test1():
    import json
    import urllib,urllib2
    import pprint
    params = {'q': '207 N. Defiance St, Archbold, OH',
            'output': 'json', 'oe': 'utf8'}
    url = 'http://maps.google.com/maps/place/' + urllib.urlencode(params)
    print urllib.urlencode(params)
    print '1600+Amphitheatre+Parkway,+Mountain+View'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View'

    raw_reply = urllib2.urlopen(url).read()
    reply = json.loads(raw_reply)

    pprint.pprint(reply)
    #print reply['Placemark'][0]['Point']['coordinates'][:-1]


def test2():
    import httplib

    path = '/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View' 

    connection = httplib.HTTPConnection('maps.googleapis.com')
    connection.request('GET', path)
    raw_reply = connection.getresponse().read()

    reply = json.loads(raw_reply)

    pprint.pprint(reply)


def test3():
    import socket
    host_name = 'google.com'
    addr = socket.gethostbyname(host_name)
    print '{} ip is {}'.format(host_name, addr)


def test4():
    import socket
    name = 'domain'
    port = socket.getservbyname(name)
    #print socket.getaddrinfo('google.com', port)
    print '{} port is {}'.format(name, port)


def udp_test1():
    import socket, sys, time
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MAX = 65535
    PORT = 1060

    if sys.argv[1:] == ['server']:
        s.bind(('127.0.0.1', PORT))
        print 'Listening at {}'.format(s.getsockname())
        while True:
            data, address = s.recvfrom(MAX)
            print 'The clinet at {} says {}'.format(address, str(data))
            s.sendto('Your data was {} bytes'.format(len(data)), address)
    elif sys.argv[1:] == ['client']:
        print 'Address before sending {}'.format(s.getsockname())
        s.sendto('This is my message', ('127.0.0.1', PORT))
        print 'Adress after sending {}'.format(s.getsockname())
        #time.sleep(10)
        data, address = s.recvfrom(MAX)
        print 'The server {} says {}'.format(address, str(data))
    else:
        print >>sys.stderr, 'usage: udp_local.py server|client'


def udp_test2():
    import socket, sys, random
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MAX = 65535
    PORT = 1060

    if sys.argv[1] == 'server' and 2 <= len(sys.argv) <=3:
        interface = sys.argv[2] if len(sys.argv) > 2 else ''
        s.bind((interface, PORT))
        print 'Listening at {}'.format(s.getsockname())
        while True:
            data, address = s.recvfrom(MAX)
            if random.randint(0, 1):
                print 'The clinet at {} says {}'.format(address, str(data))
                s.sendto('Your data was {} bytes'.format(len(data)), address)
            else:
                print 'Pretending to drop packet from {}'.format(address)
    elif sys.argv[1] == 'client' and len(sys.argv) == 3:
        host_name = sys.argv[2]
        s.connect((host_name, PORT))
        print 'Clinet socket name is {}'.format(s.getsockname())
        delay = 0.1
        while True:
            s.send('This is another message')
            print 'Wait up to {} secs'.format(delay)
            s.settimeout(delay)
            try:
                data = s.recv(MAX)
            except socket.timeout:
                delay *= 2
                if delay > 2.0:
                    raise RuntimeError('I think server is down')
            except:
                raise
            else:
                break
        print 'The server says {}'.format(str(data))
    else:
        print >>sys.stderr, 'usage: udp_local.py server|client'
        sys.exit(2)

def udp_test3():
    import socket, sys, random
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    MAX = 65535
    PORT = 1060

    if sys.argv[1] == 'server' and 2 <= len(sys.argv) <=3:
        interface = sys.argv[2] if len(sys.argv) > 2 else ''
        s.bind((interface, PORT))
        print 'Listening for broadcasts at {}'.format(s.getsockname())
        while True:
            data, address = s.recvfrom(MAX)
            print 'The client at {} says {}'.format(address, str(data))
            s.sendto('Your data was {} bytes'.format(len(data)), address)
    elif sys.argv[1] == 'client' and len(sys.argv) == 3:
        host_name = sys.argv[2]

        print 'Client socket name is {}'.format(s.getsockname())
        s.sendto('Broadcasts Message!', (host_name, PORT))
    else:
        print >>sys.stderr, 'usage: udp_local.py server|client'
        sys.exit(2)


udp_test3()



