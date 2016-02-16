#!/usr/bin/env bash

curl  -X GET http://10.192.40.29/admin/usage \
-H "Host: 10.192.40.29" \
-H "Connection: keep-alive" \
-H "Cache-Control: max-age=0" \
-H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" \
-H "Upgrade-Insecure-Requests: 1"\
-H "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36" \
-H "Accept-Encoding: gzip, deflate, sdch"\
-H "Accept-Language: zh-CN,zh;q=0.8" \
-H "Authorization: AWS Z2ETKC4RQFTR4XBQ1A72:QKkqV1z6xbhTkGgHBiVK1DJ77+g="  \
-o get_usage.out
