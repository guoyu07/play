#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os # for popen
import uuid # for random string

# I have written a bunch of py code to test RGW s3 API.
# Here I want to write a test-all py code for a whole test of these scripts.
# My idea is simple. Run script one by one and generate output files, then check whether if resulting files's content match what we expected.

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def make_pass(s):
    return bcolors.OKGREEN + s + bcolors.ENDC

def make_fail(s):
    return bcolors.FAIL + s + bcolors.ENDC

# global config
#api_host = '172.16.6.78'
api_host = '10.192.11.9'


def run_and_res(script_name, *args):
    args_expand = " ".join(args)
    res = os.popen(script_name + ' ' + args_expand).read().strip()
    return res 

def rand_str():
    return str(uuid.uuid1())

# list all buckets
res = run_and_res('./list_buckets.py', api_host)

if res == '200':
    print(make_pass('[list_buckets.py] PASS!'))
else:
    print(make_fail('[list_buckets.py] FAILED!'))
    exit()



# test create bucket
bname = rand_str()

res = run_and_res('./create_bucket.py', api_host, bname)

if res == '200':
    print(make_pass('[create_bucket.py] PASS!'))
else:
    print(make_fail('[create_bucket.py] FAILED!'))
    exit()

# test create object
oname = rand_str()
content = rand_str()

res = run_and_res('./create_object.py', api_host, bname, oname, content)

if res == '200':
    print(make_pass('[create_object.py] PASS!'))
else:
    print(make_fail('[create_object.py] FAILED!'))
    exit()

# test multi-part upload
multi_oname = rand_str()

res = run_and_res('./init_multi_part_upload.py', api_host, bname, multi_oname)

print('res:' + res)
status, upload_id = res.split(':')

if status == '200':
    print(make_pass('[init_multi_part_upload.py] PASS!'))
else:
    print(make_fail('[init_multi_part_upload.py] FAILED!'))
    exit()


for i in range(10):
    res = run_and_res('./do_multi_part_upload.py', api_host, bname, multi_oname, str(i), upload_id)

    if res == '200':
        print(make_pass('[do_multi_part_upload.py] PASS! ' + str(i)))
    else:
        print(make_fail('[do_multi_part_upload.py] FAILED! ' + str(i)))
        exit()

res = run_and_res('./list_multi_part_upload.py', api_host, bname, multi_oname, upload_id)

if res == '200':
    print(make_pass('[list_multi_part_upload.py] PASS!'))
else:
    print(make_fail('[list_multi_part_upload.py] FAILED!'))
    exit()
  
res = run_and_res('./finish_multi_part_upload.py', api_host, bname, multi_oname, upload_id)

if res == '200':
    print(make_pass('[finish_multi_part_upload.py] PASS!'))
else:
    print(make_fail('[finish_multi_part_upload.py] FAILED!'))
    exit()
 

# test get object info
res = run_and_res('./get_object_info.py', api_host, bname, oname)

if res == '200':
    print(make_pass('[get_object_info.py] PASS!'))
else:
    print(make_fail('[get_object_info.py] FAILED!'))
    exit()

# test get object
res = run_and_res('./get_object.py', api_host, bname, oname)

if res == '200':
    print(make_pass('[get_object.py] PASS!'))
else:
    print(make_fail('[get_object.py] FAILED!'))
    exit()


# test copy object
dobject = rand_str()

res = run_and_res('./copy_object.py', api_host, bname, oname, bname, dobject)

if res == '200':
    print(make_pass('[copy_object.py] PASS!'))
else:
    print(make_fail('[copy_object.py] FAILED!'))
    exit()

# test list objects in a bucket
res = run_and_res('./list_objects.py', api_host, bname)

if res == '200':
    print(make_pass('[list_objects.py] PASS!'))
else:
    print(make_fail('[list_objects.py] FAILED!'))
    exit()




# test delete object
res = run_and_res('./delete_object.py', api_host, bname, oname)

if res == '204':
    print(make_pass('[delete_object.py] PASS!'))
else:
    print(make_fail('[delete_object.py] FAILED!'))
    exit()

res = run_and_res('./delete_object.py', api_host, bname, dobject)

if res == '204':
    print(make_pass('[delete_object.py] PASS!'))
else:
    print(make_fail('[delete_object.py] FAILED!'))
    exit()

res = run_and_res('./delete_object.py', api_host, bname, multi_oname)

if res == '204':
    print(make_pass('[delete_object.py] PASS!'))
else:
    print(make_fail('[delete_object.py] FAILED!'))
    exit()



# test delete bucket
res = run_and_res('./delete_bucket.py', api_host, bname)

if res == '204':
    print(make_pass('[delete_bucket.py] PASS!'))
else:
    print(make_fail('[delete_bucket.py] FAILED!'))
    exit()
