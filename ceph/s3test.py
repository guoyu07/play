#!/usr/bin/env python

import boto
import boto.s3.connection
access_key = 'Z2ETKC4RQFTR4XBQ1A72'
secret_key = 'vqdQGtmruGW855mduffA8lsLx+ot9iXIb9QTtT2I' 
conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'ceph1',
        is_secure=False,
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)
for bucket in conn.get_all_buckets():
    print "{name}\t{created}".format(
                        name = bucket.name,
                        created = bucket.creation_date,
                        )
