def isLower(a):
    if ord(a) >= 97 and ord(a) <= 122:
        return True
    else:
        return False
n = int(input())
while n > 0:
    n -= 1
    texto = input()
    k = len(texto) - 1
    for i in range(k , -1, -1):
        if isLower(texto[i]):
            print(texto[i], end='')
    print()