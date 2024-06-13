first = True
while True:
    n = int(input())
    if n == 0:
        break
    else:
        if first == False:
            print()
    camisetas = {}
    for _ in range(n):
        nome = input().strip()
        cor, tamanho = input().split()
        chave = (cor, tamanho)
        if chave not in camisetas:
            camisetas[chave] = []
        camisetas[chave].append(nome)
    for chave in sorted(camisetas.keys(), key=lambda x: (x[0], {'P': 1, 'M': 2, 'G': 3}[x[1]])):
        cor, tamanho = chave
        nomes = sorted(camisetas[chave])
        for nome in nomes:
            print(f'{cor} {tamanho} {nome}')
    first = False