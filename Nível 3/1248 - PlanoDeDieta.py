n = int(input())
for _ in range(n):
    cheater = False
    comidas = input()
    cafe = input()
    almoco = input()
    jantarIdeal = ''
    for caractere in comidas:
        if caractere not in cafe and caractere not in almoco:
            jantarIdeal += caractere
    jantarOrdenado = sorted(jantarIdeal)
    for caractere in cafe:
        if caractere not in comidas:
            cheater = True
    for caractere in almoco:
        if caractere not in comidas:
            cheater = True
    if cheater:
        print("CHEATER")
    else:
        print(*jantarOrdenado, sep="")