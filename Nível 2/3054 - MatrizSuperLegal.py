def condicao(matriz, i, j):
    return matriz[0][0] + matriz[i][j] <= matriz[0][j] + matriz[i][0]

def matrizSuperLegal(matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    maximo = 0

    for i in range(1, linhas):
        for j in range(1, colunas):
            if condicao(matriz, i, j):
                matriz[i][j] += matriz[i-1][j-1]
                maximo = max(maximo, matriz[i][j])

    return maximo

L, C = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(L)]

result = matrizSuperLegal(matriz) - 1
print(result)