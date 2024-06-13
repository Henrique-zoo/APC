salario = float(input())

if salario <= 2000:
    imposto = "Isento"
elif salario <= 3000:
    imposto = (salario - 2000) * 0.08
elif salario <= 4500:
    imposto = 1000 * 0.08 + (salario - 3000) * 0.18
else:
    imposto = 1000 * 0.08 + 1500 * 0.18 + (salario - 4500) * 0.28
if type(imposto) == float:
    print(f"R$ {imposto:.2f}")
else:
    print(imposto)