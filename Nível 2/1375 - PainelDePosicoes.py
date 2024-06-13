while True:
    impossivel = False
    x = int(input())
    if x == 0:
        break
    carro = []
    ganhou_perdeu = []
    posicao = []
    posicaoFinal = []
    grid = [0]*x
    
    for i in range(1, x+1):
        c, p = map(int, input().split())
        posicao.append(i)
        carro.append(c)
        ganhou_perdeu.append(p)
    for j in range(len(posicao)):
        posicaoFinal.append(posicao[j] + ganhou_perdeu[j] - 1)
    for i in range(len(posicaoFinal)):
        if posicaoFinal[i] == posicaoFinal[i+1] or [elemento > len(carro) - 1 for elemento in ganhou_perdeu]:
            impossivel = True
            break
        grid[posicaoFinal[i]] = carro[i]
    if impossivel:
        print(-1)
    else:
        print(*grid)