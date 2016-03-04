#!/usr/bin/env python3
# -*- coding: utf-8 -*-

with open('./bigfile', 'w') as f:
    for i in range(2):
        for j in range(10):
            f.write(str(j))

print('Done!')
