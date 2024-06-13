def fatorial(a):
    if a > 0:
        return a * fatorial(a - 1)
    else:
        return 1

n = int(input("Digite um número natural: "))
fat = fatorial(n)
print(f"O fatorial de {n} é {fat}.")