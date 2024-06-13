'''def ordenando(a, b):
    if a > b:
        return b, a
    else:
        return a, b
def mdc(a, b):
    x = a
    while x > 1:
        if a % x == 0  and b % x == 0:
            return x
        else:
            x -= x

x, y = map(int, input().split())
z, k = ordenando(x, y)
n = mdc(z, k)

print(n)'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
x, y = map(int, input().split())
ans = gcd(x, y)

print(f"O máximo divisor comum entre {x} e {y} é {ans}")
