#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime

bname = input('bucket name:')
method = 'PUT'
content = None

with open('acl.xml', 'r') as f:
    content = f.read()

content = bytes(content, 'utf-8')
len_str = str(len(content))
#demouserid
#access_key = 'Z2ETKC4RQFTR4XBQ1A72'
#secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'

#hr
access_key = '9M3C3NCBEWSRDPRJGL0O'
secret_key = 'QCS0ju6dkqblLVQe966KwuE2Cg6cCfS/S2u2K+Qt'

#eleme
#access_key = "VI8LSAC5JOFE99B066FC"
#secret_key = "m6ok1UbM+eTBqXXHRsAJ6PbUh3fmZDDfmOnHKk3M"

req = Request('http://10.192.40.29/' + bname + '?acl', data = content,
            method = method)
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', '10.192.40.29')
req.add_header('Date', timestr)
#req.add_header('x-amz-acl', 'public-read-write')
#req.add_header('Content-Type', 'application/xml')
#req.add_header('Content-Length', str(len(content)))

m = hashlib.md5()
m.update(content)
md5value = base64.b64encode(m.digest()).decode('utf-8')

req.add_header('Content-Type', 'application/xml')
req.add_header('Content-Length', len_str)
req.add_header('Content-MD5', md5value)

hstr = ''
hstr += method + '\n'
hstr += md5value + '\n'
hstr += 'application/xml\n'
hstr += timestr + '\n'

hstr += 'Content-Length:' + len_str + '\n'
#hstr += 'Content-Type: application/xml\n'
#hstr += 'Content-Length: ' + str(len(content)) + '\n'
hstr += '/' + bname + '?acl'
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


