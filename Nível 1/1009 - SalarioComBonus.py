nome= input()
salario = float(input())
vendas = float(input())

bonus = 0.15*vendas

renda = salario + bonus

print(f'TOTAL = R$ {renda:.2f}')