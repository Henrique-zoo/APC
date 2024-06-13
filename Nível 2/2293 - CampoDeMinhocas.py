n, m = map(int, input().split())
minhocasColhidas = []
matriz = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
for i in range(n):
    minhocas = 0
    for j in range(m):
        minhocas += matriz[i][j]
    minhocasColhidas.append(minhocas)
for j in range(m):
    minhocas = 0
    for i in range(n):
        minhocas += matriz[i][j]
    minhocasColhidas.append(minhocas)
print(max(minhocasColhidas))