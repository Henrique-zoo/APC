n = int(input())
matriz = [[0]*(n+3)]
matrizFinal = []
for i in range(1, n+2):
    linha = list(map(int, ('0 ' + input() + ' 0').split()))
    matriz.append(linha)
matriz.append([0]*(n+3))
for i in range(1, n+1):
    linha = []
    for j in range(1, n+1):
        if (matriz[i][j] + matriz[i+1][j] + matriz[i][j+1] + matriz[i+1][j+1]) >= 2:
            linha.append('S')
        else:
            linha.append('U')
    matrizFinal.append(linha)
for linha in matrizFinal:
    print(*linha, sep='')