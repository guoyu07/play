#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib.request import Request
import random

#http://www.jyeoo.com/math/ques/partialques?q=75a08844-6562-4bf5-a182-034cf7929588~4e1c9a08-d989-45c8-b89f-097da57cbd75~&f=0&ct=0&dg=0&fg=0&po=0&pd=1&pi=1&r=0.06341112940572202

#http://www.jyeoo.com/math/ques/partialques?q=75a08844-6562-4bf5-a182-034cf7929588~4e1c9a08-d989-45c8-b89f-097da57cbd75~&f=0&ct=0&dg=0&fg=0&po=0&pd=1&pi=2&r=0.7151490014512092

#http://www.jyeoo.com/math/ques/partialques?q=75a08844-6562-4bf5-a182-034cf7929588~4e1c9a08-d989-45c8-b89f-097da57cbd75~&f=0&ct=0&dg=0&fg=0&po=0&pd=1&pi=3&r=0.09438273264095187
for p in range(1, 101):
    # iterate over pages from 1 to 100
    req = Request('http://www.jyeoo.com/math/ques/partialques?q=75a08844-6562-4bf5-a182-034cf7929588~4e1c9a08-d989-45c8-b89f-097da57cbd75~&f=0&ct=0&dg=0&fg=0&po=0&pd=1&pi='+ str(p) + '&r=' + str(random.random()), method = 'GET')
    
    req.add_header('Accept', 'text/html, */*; q=0.01')
#    req.add_header('Accept-Encoding', 'gzip, deflate, sdch')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.8')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Host', 'www.jyeoo.com')
    req.add_header('Referer', 'http://www.jyeoo.com/math/ques/search')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36')
    req.add_header('X-Requested-With', 'XMLHttpRequest')

    with urllib.request.urlopen(req) as fin, open(str(p) + '.html', 'w') as fout:
        fout.write(fin.read().decode('utf-8'))
        #print(fin.read().decode('utf-8'))
    print('done with p:%d' % (p, ))
