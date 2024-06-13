dia = input().split()[1]
dia = int(dia)
hora, minuto, segundo = map(int, input().split(':'))

dia2 = input().split()[1]
dia2 = int(dia2)
hora2, minuto2, segundo2 = map(int, input().split(':'))

tempo = dia*24*3600 + hora*3600 + minuto*60 + segundo
tempo2 = dia2*24*3600 + hora2*3600 + minuto2*60 + segundo2
duracao = tempo2 - tempo
dias = duracao // (24*3600)
horas = duracao % (24*3600) // 3600
minutos = (duracao % (24*3600) % 3600) // 60
segundos = (duracao % (24*3600) % 3600) % 60
print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')