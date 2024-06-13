H1, M1, H2, M2 = map(int, input().split())

tempo1 = H1*60 + M1
tempo2 = H2*60 + M2
if tempo2 <= tempo1:
    tempo2 = tempo2 + 24*60
duracao = tempo2 - tempo1
hora = duracao//60
min = duracao%60

print(f"O JOGO DUROU {hora} HORA(S) E {min} MINUTO(S)")