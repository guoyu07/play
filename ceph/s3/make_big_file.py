#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('./5M', 'w') as f:
    for i in range(1000*1000):
        for j in range(6):
            f.write(str(j))

print('Done!')
