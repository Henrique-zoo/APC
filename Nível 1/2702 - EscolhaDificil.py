def seFoderam(x, y):
    if y > x:
        return y - x
    else:
        return 0

x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

resto = seFoderam(x, a) + seFoderam(y, b) + seFoderam(z, c)

print(resto)