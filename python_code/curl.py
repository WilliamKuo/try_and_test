import pprint
import uuid
import datetime
import os 
import inspect
import time
import json
import requests

# get

#url = 'http://10.90.6.90:8282/v1/compute/os-floating-ips'
#headers = {'X-Auth-Token':'94bfc3e7a61e4fd9abf02ad3068a1bab'}
#
#r = requests.get(url, headers=headers)
#
#pprint.pprint(r.headers)
#pprint.pprint(json.loads(r.text))


# create post

#url = 'http://10.90.6.90:8282/v1/application/apps/abe49b1f-35b1-4516-94dc-a9126fc2edcf/pools/f66c7531-84ee-48f3-b938-a0343955cdb2/volumes'
#data = {"mode":"exact_match","name":"TEST4","performance":"LOW","capacity":1048576,"raid_type":-1}
#headers = {'X-Auth-Token':'94bfc3e7a61e4fd9abf02ad3068a1bab', 'Content-Type':'application/json'}
#
#r = requests.post(url, headers=headers, data=json.dumps(data))
#pprint.pprint(r.headers)
#pprint.pprint(json.loads(r.text))




# delete

url = 'http://10.90.6.90:8282/v1/application/apps/abe49b1f-35b1-4516-94dc-a9126fc2edcf/pools/f66c7531-84ee-48f3-b938-a0343955cdb2/volumes/6a53acb3-23b1-4bfa-9b41-c6f7dbca2be9'
headers = {'X-Auth-Token':'94bfc3e7a61e4fd9abf02ad3068a1bab'}

r = requests.delete(url, headers=headers)
print r.status_code
pprint.pprint(r.headers)
#pprint.pprint(json.loads(r.text))




















