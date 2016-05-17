#!/usr/bin/env python

T = int(raw_input())
for _t in range(1, T + 1):
    act_num, origin = raw_input().split();
    act_num = int(act_num)
    
    got = 0
    for i in range(act_num):
        line = raw_input()
        handle = line[0:9]
        if handle == 'CONTEST_H':
            got += 50
        elif handle == 'BUG_FOUND':
            _, severity = line.split()
            ser = int(severity)
            got += ser
        elif handle == 'TOP_CONTR':
            got += 300
        else: # contest won
            _, rank = line.split()
            rank = int(rank)
            got += 300
            if rank <= 20:
                got += (20 - rank)

    if origin == 'INDIAN':
        print '%d' % (got/200,)
    else:
        print '%d' % (got/400,)
