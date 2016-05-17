import sys 
print '1'
print '2 1 2'
print '3 3 4 5'
sys.stdout.flush()
res = int(raw_input())

if res >= 0:
    # try 1 2
    print '1'
    print '1 1'
    print '1 2'
    sys.stdout.flush()
    res = int(raw_input())
    if res > 0:
        print '2'
        print '1'
    else:
        print '2'
        print '2'
else:
    # try 3 4 5
    print '1'
    print '2 3 4'
    print '1 5'
    sys.stdout.flush()
    res = int(raw_input())
    if res == 0:
        print '2'
        print '5'
    else:
        print '1'
        print '1 3'
        print '1 4'
        sys.stdout.flush()
        res = int(raw_input())
        if res > 0:
            print '2'
            print '3'
        else:
            print '2'
            print '4'
