import pprint
import uuid
import datetime
import os 
import inspect
import time
import json
import requests

def print_result(r):
    print 'status:{}'.format(r.status_code)
    print 'header:{}'.format(r.headers)
    print 'text  :{}'.format(r.text)


url = 'http://ec2-13-231-188-201.ap-northeast-1.compute.amazonaws.com/'
url = 'http://127.0.0.1:5000/'

def test_loop():
    for i in xrange(3):
        _url = url + str(i)
        print '================'
        
        r = requests.get(_url)
        print_result(r)

        data = {'test_data': 'test', 'no_used': 'aaaaaaa'}
        r = requests.post(_url, data=json.dumps(data))
        #r = requests.post(_url, data=data)
        print_result(r)

        r = requests.delete(_url)
        print_result(r)

# print requests.__version__
print '\n\n\n\n\n\n\n\n\n'
test_loop()





