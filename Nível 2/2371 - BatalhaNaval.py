n, m = map(int, input().split())
campo = []
for _ in range(n):
    linha = [x for x in input()]
    campo.append(linha)
k = int(input())
partes = []
for _ in range(k):
    l, c = map(int, input().split())
    if campo[l-1][c-1] == '#':
        partes.append([l,c])
count = len(partes)
for i in range(len(partes)):
    for j in range(1, len(partes)-1):
        if partes[i][1] == partes[j][1] and (partes[i][0] == partes[j][0]+1 or partes[i][0] == partes[j][0]-1):
            count -= 1
    if partes[i][0] == partes[i-1][0] and partes[i][1] == partes[i-1][1]+1:
        count -= 1
print(count)