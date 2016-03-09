#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime

#name, content = input().split()
name = input()

access_key = 'Z2ETKC4RQFTR4XBQ1A72'
secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'

content = None
with open('./acl.xml', 'r') as f:
    content = f.read()
content = bytes(content, 'utf-8')

req = Request('http://10.192.40.29/public/' + name + '?acl', data = content,
            method = 'PUT')
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', '10.192.40.29')
req.add_header('Date', timestr)
# req.add_header('x-amz-acl', 'public-read-write')
#m = hashlib.md5()
#m.update(content)
#md5value = base64.b64encode(m.digest()).decode('utf-8')

req.add_header('Content-Type', 'application/xml')
req.add_header('Content-Length', str(len(content)))
#req.add_header('Content-MD5', md5value)

hstr = ''
hstr += 'PUT\n'
hstr += '\n'
hstr += '\n'
hstr += timestr + '\n'
hstr += 'Content-Type: application/xml\n'  
hstr += 'Content-Length: ' + str(len(content)) + '\n'
# hstr += 'x-amz-acl:public-read-write\n'
hstr += '/public/' + name + '?acl'
print('hstr:%s' % (hstr,))

key = bytearray(secret_key, 'utf-8')
hres = hmac.new(key, hstr.encode('utf-8'), hashlib.sha1).digest()
print('type:%s' % (type(hres, )))

hres = base64.b64encode(hres)

hres = hres.decode('utf-8')
print('hres:%s' % (hres,))

req.add_header('Authorization', 'AWS ' + access_key + ':' + hres)


with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))


