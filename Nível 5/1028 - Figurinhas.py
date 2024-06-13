def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
n = int(input())
while n > 0:
    n -= 1
    f1, f2 = map(int, input().split())
    tamanho = gcd(f1, f2)
    print(tamanho)