notas = [100, 50, 20, 10, 5, 2]
moedas = [50, 25, 10, 5, 1] 
qtdNotas = []
qtdMoedas = []

N = float(input())
M = int((N - int(N))*100)
for nota in notas:
    K = int(N)
    qtd = K // nota
    qtdNotas.append(qtd)
    N = N % nota

moeda1 = K % 2
for moeda in moedas:
    qtd = M // moeda
    qtdMoedas.append(qtd)
    M = M % moeda
     
textosNotas = ["nota(s) de R$ 100.00", "nota(s) de R$ 50.00", "nota(s) de R$ 20.00", "nota(s) de R$ 10.00", "nota(s) de R$ 5.00", "nota(s) de R$ 2.00"]
textosMoedas = ["moeda(s) de R$ 0.50", "moeda(s) de R$ 0.25", "moeda(s) de R$ 0.10", "moeda(s) de R$ 0.05", "moeda(s) de R$ 0.01"]

print('NOTAS:')
for i in range(len(notas)):
    print(f"{qtdNotas[i]} {textosNotas[i]}")
    
print('MOEDAS:')
print(f'{moeda1} moeda(s) de R$ 1.00')
for i in range(len(moedas)):
    print(f"{qtdMoedas[i]} {textosMoedas[i]}")
