n = int(input())
lista = input().split()
menor_valor = int(lista[0])
posicao = 0
for i in range(1, n):
    if int(lista[i]) < menor_valor:
        menor_valor = int(lista[i])
        posicao = i

print(f"Menor valor: {menor_valor}\nPosicao: {posicao}")