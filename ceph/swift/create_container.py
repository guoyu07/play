#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime
import sys

# demouserid
#access_key = 'Z2ETKC4RQFTR4XBQ1A72'
#secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'

#host_port = '172.16.6.81:7480'
#host_port = '10.192.40.29'

#hr
#access_key = "9M3C3NCBEWSRDPRJGL0O"
#secret_key = "QCS0ju6dkqblLVQe966KwuE2Cg6cCfS/S2u2K+Qt"

# demo from local vcenter
user = 'demo:swift'
key = 'AUTH_rgwtk0a00000064656d6f3a737769667405c76213d8f0b9ed363630575fb9ba16581f0f8c9e47c897a41b24696fa9cf1a744d8de1'
#content = None

#with open('./test03.xls', 'rb') as f:
#    content = f.read()

req = Request('http://172.16.6.78/swift/v1/registry', 
            method = 'PUT')
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', '172.16.6.78')
req.add_header('Date', timestr)
#req.add_header('x-amz-acl', 'public-read-write')
req.add_header('X-Auth-Token', key)





with urllib.request.urlopen(req) as f:
    print(f.status)
    print(f.read().decode('utf-8'))


