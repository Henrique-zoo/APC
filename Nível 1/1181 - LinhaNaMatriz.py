linhaEscolhida = int(input())
operacao = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
soma = 0
for linha in range(len(matriz)):
    if linha == linhaEscolhida:
        for elemento in matriz[linha]:
            soma += elemento
        if operacao == "S":
            ans = soma
        else:
            ans = soma/12
print(ans)