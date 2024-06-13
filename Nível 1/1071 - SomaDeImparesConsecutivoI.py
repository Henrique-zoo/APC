'''def impares(a, b):
    if a <= b:
        return 0
    if b % 2 == 0:
        b += 1
    return b + impares(a, b + 2)

def sort(a, b):
    if a >= b:
        return a, b
    else:
        return b, a

x = int(input())
y = int(input())

x, y = sort(x, y)
soma = impares(x, y + 1)
print(soma)'''

def impares(a, b):
    sum = 0
    while a > b:
        if b % 2 == 0:
            b += 1
        sum = b + sum
        b +=2
    return sum

def sort(a, b):
    if a >= b:
        return a, b
    else:
        return b, a

x = int(input())
y = int(input())

x, y = sort(x, y)
soma = impares(x, y + 1)
print(soma)