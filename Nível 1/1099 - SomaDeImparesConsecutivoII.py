def minemax(a, b):
    if a >= b:
        return b, a
    else:
        return a, b

n = int(input())
while n > 0:
    n -= 1
    ans = 0
    x, y = map(int, input().split())
    x, y = minemax(x, y)
    if x % 2 == 0:
        x = x + 1
    else:
        x = x + 2
    for i in range(x, y, 2):
        ans += i
        
    print(ans)