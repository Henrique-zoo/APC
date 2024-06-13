i, par, impar, positivo, negativo = 0, 0, 0, 0, 0
while i < 5:
    i += 1
    x = int(input())
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
    if x > 0:
        positivo += 1
    elif x < 0:
        negativo += 1
print(f'''{par} valor(es) par(es)
{impar} valor(es) impar(es)
{positivo} valor(es) positivo(s)
{negativo} valor(es) negativo(s)''')