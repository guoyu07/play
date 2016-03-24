#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime


req = Request('http://10.192.40.29/' + bname + '/' + name, data=content,
            method = 'PUT')
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', '10.192.40.29')
req.add_header('Date', timestr)
req.add_header('x-amz-acl', 'public-read-write')
req.add_header('Content-Type', 'text/plain')
req.add_header('Content-MD5', md5value)
req.add_header('Authorization', 'AWS ' + access_key + ':' + hres)


with urllib.request.urlopen(req) as f:
    print(f.read().decode('utf-8'))


