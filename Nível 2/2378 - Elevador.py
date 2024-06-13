n, c = map(int, input().split())
p = 0
while n > 0:
    s, e = map(int, input().split())
    if p <= c:
        p += e
        p -= s
    else:
        break
    n -= 1
    
if p > c:
    print('S')
else:
    print('N')