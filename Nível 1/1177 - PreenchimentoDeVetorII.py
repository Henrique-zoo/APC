t = int(input())
x = 1000
lista = []
while x > 0:
    x -= 3
    for k in range(0, t):
        if len(lista) == 1000:
            break
        lista.append(k)
for i in range(len(lista)):
    print(f"N[{i}] = {lista[i]}")