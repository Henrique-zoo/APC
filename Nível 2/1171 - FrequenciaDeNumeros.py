n = int(input())
dicionario = {}
for _ in range(n):
    x = int(input())
    if x in dicionario:
        dicionario[x] += 1
    else:
        dicionario[x] = 1
chavesOrdenadas = sorted(dicionario)
for chave in chavesOrdenadas:
    print(f'{chave} aparece {dicionario[chave]} vez(es)')