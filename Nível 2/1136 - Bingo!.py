def pode_anunciar_todos_numeros(N, B, bolas):
    bolas.sort()
    numeros_anunciados = set()
    for i in range(B):
        for j in range(i, B):
            diferenca = abs(bolas[i] - bolas[j])
            numeros_anunciados.add(diferenca)
    for numero in range(N + 1):
        if numero not in numeros_anunciados:
            return 'N'
    return 'Y'

while True:
    N, B = map(int, input().split())
    if N == 0 and B == 0:
        break
    bolas = list(map(int, input().split()))
    resultado = pode_anunciar_todos_numeros(N, B, bolas)
    print(resultado)
