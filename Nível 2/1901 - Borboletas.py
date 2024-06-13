n = int(input())
matriz = []
matrizFinal = []
for _ in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
for _ in range(n*2):
    l, c = map(int, input().split())
    l = l-1; c = c-1
    if matriz[l][c] not in matrizFinal:
        matrizFinal.append(matriz[l][c])
print(len(matrizFinal))