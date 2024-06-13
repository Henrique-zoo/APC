a = g = d = 0
while True:
    x = int(input())
    if x == 4:
        break
    elif x == 1:
        a += 1
    elif x == 2:
        g += 1
    elif x == 3:
        d += 1
print(f'''MUITO OBRIGADO
Alcool: {a}
Gasolina: {g}
Diesel: {d}''')