#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import hmac
import hashlib
import base64 
import datetime
import sys
import xml.dom.minidom as dom # for xml parsing and generating

if len(sys.argv) < 5:
    print('bad syntax, usage: {script_name} host bucket object uploadId')
    exit()


host, bkt, obj, upload_id = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
# demouserid
#access_key = 'Z2ETKC4RQFTR4XBQ1A72'
#secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I'

# demo from local vcenter
#access_key = 'YG9YGNNYN46ARJH1MOEJ'
#secret_key = 'mxzTzqF7XZx00hmy7n4qzUQ5mKinYywuRD2xV4ka'
# demo from wx
access_key = '73SAVVNQIIKSJCIFUDZF'
secret_key = 'aZCMX8DwqSRIx4MgFbCctMNlyZTld28aeYhsDZYM'


#hr
#access_key = "9M3C3NCBEWSRDPRJGL0O"
#secret_key = "QCS0ju6dkqblLVQe966KwuE2Cg6cCfS/S2u2K+Qt"

#eleme
#access_key = 'VI8LSAC5JOFE99B066FC'
#secret_key = 'm6ok1UbM+eTBqXXHRsAJ6PbUh3fmZDDfmOnHKk3M'


req = Request('http://' + host + '/' + bkt + '/' + obj + '?uploadId=' + upload_id, 
        method = 'GET')
timestr = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')

req.add_header('Host', host)
req.add_header('Date', timestr)
#req.add_header('x-amz-acl', 'public-read-write')

# md5 content
#m = hashlib.md5()
#m.update(content)
#md5value = base64.b64encode(m.digest()).decode('utf-8')

#req.add_header('Content-Type', 'text/plain')
#req.add_header('Content-MD5', md5value)

hstr = ''
hstr += 'GET\n'
hstr += '\n'
hstr += '\n'
hstr += timestr + '\n'
#hstr += 'x-amz-acl:public-read-write\n'
hstr += '/' + bkt + '/' + obj + '?uploadId=' + upload_id
#print('hstr:%s' % (hstr,))

key = bytearray(secret_key, 'utf-8')
hres = hmac.new(key, hstr.encode('utf-8'), hashlib.sha1).digest()
#print('type:%s' % (type(hres, )))

hres = base64.b64encode(hres)

hres = hres.decode('utf-8')
#print('hres:%s' % (hres,))

req.add_header('Authorization', 'AWS ' + access_key + ':' + hres)


with urllib.request.urlopen(req) as f:
    raw_str = f.read().decode('utf-8')
    if f.status == 200:
        d = dom.parseString(raw_str)
        parts = d.getElementsByTagName('Part')
        
        tmp = '<CompleteMultipartUpload>'
        for part in parts:
            tmp += part.toxml()
        tmp += '</CompleteMultipartUpload>'

        with open('./finish.xml', 'w') as fout:
            fout.write(tmp)

    print(f.status)

    

