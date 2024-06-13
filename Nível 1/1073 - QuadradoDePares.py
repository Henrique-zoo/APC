def quadrados(a):
    if a > 0:
        quadrados(a - 2)
        print(f'{a}^2 = {a**2}')
quadrados(int(input()))