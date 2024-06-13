n = int(input())
pares = []
impares = []

for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)
pares.sort()
impares.sort(reverse=True)
for i in pares:
    print(i)
for j in impares:
    print(j)