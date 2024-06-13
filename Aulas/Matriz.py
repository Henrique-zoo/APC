n, m = map(int, input().split())
matriz = []
for _ in range(0, n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
for i in range(0, m):
    print(matriz[i])