#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime

bname, pre, sep = input('bname pre sep:\n').split()
# demouserid
#access_key = 'Z2ETKC4RQFTR4XBQ1A72'
#secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'

# hr
access_key = "9M3C3NCBEWSRDPRJGL0O"
secret_key = "QCS0ju6dkqblLVQe966KwuE2Cg6cCfS/S2u2K+Qt"

req = Request('http://10.192.40.29/' + bname + '?prefix='+ pre + '&delimiter=' + sep ,
            method = 'GET')
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', '10.192.40.29')
req.add_header('Date', timestr) 

hstr = ''
hstr += 'GET\n'
hstr += '\n'
hstr += '\n'
hstr += timestr + '\n'
hstr += '/' + bname
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


