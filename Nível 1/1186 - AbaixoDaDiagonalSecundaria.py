operacao = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
qtdSomada = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j + i >= len(matriz[i]):
            soma += matriz[i][j]
            qtdSomada += 1
if operacao == 'S':
    resposta = soma
else:
    resposta = soma/qtdSomada
print(f'{resposta:.1f}')