n = int(input())
lista = [int(x) for x in input().split()]
count = 1
for i in range(1, len(lista)-1):
    if lista[i] - lista[i+1] != lista[i-1]- lista[i]:
        count += 1
print(count)