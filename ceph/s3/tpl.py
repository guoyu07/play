#!/usr/bin/env python3

import urllib.request.Request as Request

req = Request('http://10.192.40.29',
            headers = {},
            method = 'GET'
        )

with urllib.request.urlopen(req) as f:
    print f.read().decode('utf-8')


