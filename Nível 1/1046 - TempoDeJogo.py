inicio, final = map(int, input().split())

if inicio >= final:
    final = final + 24

duracao = final - inicio
print(f"O JOGO DUROU {duracao} HORA(S)")