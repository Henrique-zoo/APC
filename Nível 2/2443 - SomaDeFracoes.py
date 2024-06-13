def gdc(x, y):
    if y == 0:
        return x
    else:
        return gdc(y, x % y)
a, b, c, d = map(int, input().split())
e = a * d + c * b
f = b * d
k = gdc(e, f)
f = f // k
e = e // k

print(e, f)