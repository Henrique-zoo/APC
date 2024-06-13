def maior(x, y):
    if y > x:
        return y
    else:
        return x

def iterando(a):
    if a == 1:
        return 1
    if a % 2 != 0:
        h = 3 * a + 1
    else:
        h = a // 2
    return maior(iterando(h), a)

n = int(input())
while n != 0:
    ans = iterando(n)
    print(ans)
    n = int(input())