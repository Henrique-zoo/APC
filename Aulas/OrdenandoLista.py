lista = input().split()
n = len(lista)
for i in range(n):
    for j in range(i+1, n):
        if lista[j] < lista[i]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print(lista)