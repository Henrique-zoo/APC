def refri(total, c):
    if total >= c:
        garrafas = total // c + total % c
        return total // c + refri(garrafas, c)
    else:
        return 0
    
e, f, c = map(int, input().split())
total = e + f
resultado = refri(total, c)
print(resultado)