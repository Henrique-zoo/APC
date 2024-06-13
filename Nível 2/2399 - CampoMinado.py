n = int(input())
lista = [0]*(n+2)
listaFinal = []
for i in range(1, n+1):
    lista[i] = int(input())
for i in range(1, n+1):
    listaFinal.append(lista[i] + lista[i-1] + lista[i+1])
print(*listaFinal, sep='\n')