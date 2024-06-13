n = int(input('Quantas matérias você fez?\n'))
divisor = 0
dividendo = 0
for i in range(n):
    materia = input(f'Qual é o nome da {i+1}º matéria? ')
    semestre = int(input(f'Em qual semestre você fez {materia}? '))
    horas = int(input(f'{materia} tem quantas horas por semestre? '))
    creditos = horas//15
    mencao = input(f'Qual foi a sua menção em {materia}? ').upper()
    if mencao == 'SS':
        valor = 5
    elif mencao == 'MS':
        valor = 4
    elif mencao == 'MM':
        valor = 3
    elif mencao == 'MI':
        valor = 2
    elif mencao == 'II':
        valor = 1
    elif mencao == 'SR':
        valor = 0
    divisor += creditos * semestre
    dividendo += valor * creditos * semestre
print(f'O seu IRA é {dividendo/divisor:.2f}')