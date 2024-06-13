def criaMatriz(d):
    matriz = []
    for _ in range(d):
        presenca = input().split()
        matriz.append(presenca)
    return matriz

def verificaPresenca(a, d, n):
    presenca =  False
    for j in range(n):
        if presenca:
            break
        presenca = True
        for i in range(d):
            if a[i][j] == '0':
                presenca = False
                break
    return presenca
                
n, d = map(int, input().split())
while n != 0 and d != 0:
    matriz = criaMatriz(d)
    presenca = verificaPresenca(matriz, d, n)
    if presenca:
        print('yes')
    else:
        print('no')
    n, d = map(int, input().split())