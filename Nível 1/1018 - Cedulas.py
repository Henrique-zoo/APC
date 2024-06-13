valores = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

N = float(input())
print(int(N))
for valor in valores:
    qtd = N // valor
    quantidades.append(qtd)
    N = N % valor

textos = ["nota(s) de R$ 100,00", "nota(s) de R$ 50,00", "nota(s) de R$ 20,00",
"nota(s) de R$ 10,00", "nota(s) de R$ 5,00", "nota(s) de R$ 2,00",
"nota(s) de R$ 1,00"]

for i in range(len(valores)):
    print(f"{int(quantidades[i])} {textos[i]}")