import math
N, W, L = map(int, raw_input())
H, R = [], []
dmax, s0 = 0, 0

for i in range(N):
    th, tr = map(int, raw_input().split())
    H.append(th)
    R.append(tr)

    tmp = 0
    if th >= L:
        tmp = 0
    else:
        tmp = math.ceil((L - th)/1.0/tr)
    dmax = max(dmax, tmp)
    
dmax += 2


