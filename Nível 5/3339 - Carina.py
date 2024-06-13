q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans = 0
    for i in range(l, r+1):
        raiz = int(i**(1/2))
        if raiz**2 == i:
            ans += 1
    print(ans)