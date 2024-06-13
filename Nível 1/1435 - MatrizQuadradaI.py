while True:
    n = int(input())
    linha = []
    coluna = []
    if n == 0: 
        break
    for i in range(n):
        linha.append(i)
        coluna.append(linha)
            
    print(coluna)