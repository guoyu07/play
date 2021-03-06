#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime
import sys

if len(sys.argv) < 4:
    print('bad syntax, usage: {script_name} host bname oname')
    exit()

host, bname, oname = sys.argv[1], sys.argv[2], sys.argv[3]

method = 'DELETE'
# demouserid
#access_key = 'Z2ETKC4RQFTR4XBQ1A72'
#secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'

#hr
#access_key = "9M3C3NCBEWSRDPRJGL0O"
#secret_key = "QCS0ju6dkqblLVQe966KwuE2Cg6cCfS/S2u2K+Qt"

# demo from local vcenter
#access_key = 'YG9YGNNYN46ARJH1MOEJ'
#secret_key = 'mxzTzqF7XZx00hmy7n4qzUQ5mKinYywuRD2xV4ka'
# demo from wx
access_key = '73SAVVNQIIKSJCIFUDZF'
secret_key = 'aZCMX8DwqSRIx4MgFbCctMNlyZTld28aeYhsDZYM'



#eleme
#access_key = 'VI8LSAC5JOFE99B066FC'
#secret_key = 'm6ok1UbM+eTBqXXHRsAJ6PbUh3fmZDDfmOnHKk3M'

req = Request('http://' + host + '/' + bname + '/' + oname,
            method = method)
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', host)
req.add_header('Date', timestr)
#req.add_header('x-amz-acl', 'public-read-write')

hstr = ''
hstr += method + '\n'
hstr += '\n'
hstr += '\n'
hstr += timestr + '\n'
#hstr += 'x-amz-acl:public-read-write\n'
hstr += '/' + bname + '/' + oname
#print('hstr:%s' % (hstr,))

key = bytearray(secret_key, 'utf-8')
hres = hmac.new(key, hstr.encode('utf-8'), hashlib.sha1).digest()
#print('type:%s' % (type(hres, )))

hres = base64.b64encode(hres)

hres = hres.decode('utf-8')
#print('hres:%s' % (hres,))

req.add_header('Authorization', 'AWS ' + access_key + ':' + hres)


with urllib.request.urlopen(req) as f:
    #print(f.read().decode('utf-8'))
    print(f.status)

