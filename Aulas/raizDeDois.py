def raizdeDois(n):
    if n > 0:
        x = 1 / (2 + raizdeDois(n-1))
        return x
    else:
        return 0

a = int(input())
raiz = 1 + raizdeDois(a)
prova = raiz**2
diferença = abs(2 - prova)

print(f"A raiz quadrada aproximada é {raiz:.30f}\nO quadrado dessa raiz aproximada é {prova:.30f}\nA diferença de 2 para esse resultado é {diferença:.30f}")