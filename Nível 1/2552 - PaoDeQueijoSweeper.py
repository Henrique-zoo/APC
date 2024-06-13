while True:
    try:
        n, m = map(int, input().split())
        matriz = []
        for _ in range(n+2):
            matriz.append([0]*(m+2))
        for i in range(1, n+1):
            linha = ['0'] + input().split() + ['0']
            for j in range(len(linha)):
                linha[j] = int(linha[j])
            matriz[i] = linha
        resposta = [[9] * m for _ in range(n)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if matriz[i][j] == 0:
                    resposta[i-1][j-1] = (matriz[i-1][j] + matriz[i][j-1] + matriz[i][j+1] + matriz[i+1][j])
        for linha in resposta:
            print(*linha, sep='')
    except EOFError:
        break