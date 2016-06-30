#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime
import sys

if len(sys.argv) < 6:
    print('bad syntax, usage: {script_name} bname oname part_id upload_id')
    exit()

host, bkt, obj, part_id, upload_id = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

# demouserid
#access_key = 'Z2ETKC4RQFTR4XBQ1A72'
#secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'
# demo from wx
access_key = '73SAVVNQIIKSJCIFUDZF'
secret_key = 'aZCMX8DwqSRIx4MgFbCctMNlyZTld28aeYhsDZYM'


# demo from local vcenter
#access_key = 'YG9YGNNYN46ARJH1MOEJ'
#secret_key = 'mxzTzqF7XZx00hmy7n4qzUQ5mKinYywuRD2xV4ka'


#hr
#access_key = "9M3C3NCBEWSRDPRJGL0O"
#secret_key = "QCS0ju6dkqblLVQe966KwuE2Cg6cCfS/S2u2K+Qt"

#eleme
#access_key = 'VI8LSAC5JOFE99B066FC'
#secret_key = 'm6ok1UbM+eTBqXXHRsAJ6PbUh3fmZDDfmOnHKk3M'

# make content

content = None
with open('5M', 'r') as fin:
    content = fin.read()

content = bytes(content, 'utf-8')

req = Request('http://' + host + '/' + bkt + '/' + obj + '?partNumber=' + part_id + '&uploadId=' + upload_id, method = 'PUT', data=content)
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', host)
req.add_header('Date', timestr)
req.add_header('x-amz-acl', 'public-read-write')

# md5 content
m = hashlib.md5()
m.update(content)
md5value = base64.b64encode(m.digest()).decode('utf-8')

req.add_header('Content-Type', 'text/plain')
req.add_header('Content-MD5', md5value)

hstr = ''
hstr += 'PUT\n'
hstr += md5value + '\n'
hstr += 'text/plain\n'
hstr += timestr + '\n'
hstr += 'x-amz-acl:public-read-write\n'
hstr += '/' + bkt + '/' + obj + '?partNumber=' + part_id + '&uploadId=' + upload_id
# print('hstr:%s' % (hstr,))

key = bytearray(secret_key, 'utf-8')
hres = hmac.new(key, hstr.encode('utf-8'), hashlib.sha1).digest()
# print('type:%s' % (type(hres, )))

hres = base64.b64encode(hres)

hres = hres.decode('utf-8')
# print('hres:%s' % (hres,))

req.add_header('Authorization', 'AWS ' + access_key + ':' + hres)


with urllib.request.urlopen(req) as f:
#    print(f.read().decode('utf-8'))
    print(f.status)

