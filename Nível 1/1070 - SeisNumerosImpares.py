def impares(a, b):
    if b <= 6:
        if a % 2 == 0:
            a += 1
        print(a)
        impares(a + 2, b +1)
x = int(input())
y = 1
impares(x, y)