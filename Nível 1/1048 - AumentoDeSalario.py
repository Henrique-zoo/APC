salario = float(input())

if salario <= 400.00:
    novoSalario = salario + 0.15 * salario
elif salario <= 800.00:
    novoSalario = salario + 0.12 * salario
elif salario <= 1200.00:
    novoSalario = salario + 0.1 * salario
elif salario <= 2000.00:
    novoSalario = salario + 0.07 * salario
else:
    novoSalario = salario + 0.04 * salario
    
reajuste = novoSalario - salario
porcentagem = round(reajuste / salario * 100)
print(f'''Novo salario: {novoSalario:.2f}
Reajuste ganho: {reajuste:.2f}
Em percentual: {porcentagem} %''')