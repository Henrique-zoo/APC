n = int(input())
while n > 0:
    n -= 1
    x = int(input())
    soma = 0
    for i in range(1, x):
        if x % i == 0:
            soma += i
    if soma == x:
        print(f"{x} eh perfeito")
    else:
        print(f'{x} nao eh perfeito')