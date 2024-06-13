n = int(input())
for _ in range(n):
    texto = input()
    textoFinal = ''
    frequencias = {}
    for letra in texto:
        if ord(letra) >= 65 and ord(letra) <= 90:
            letra = chr(ord(letra) + 32)
        textoFinal += letra
    for caractere in textoFinal:
        if caractere != ' ':
            if caractere in frequencias:
                frequencias[caractere] += 1
            else:
                frequencias[caractere] = 1
    alfabetico = sorted(frequencias)
    numero = 0
    for letra in frequencias:
        if frequencias[letra] > numero:
            numero = frequencias[letra]
    resposta = ''
    for letra in alfabetico:
        if frequencias[letra] == numero:
            resposta += letra
    print(resposta)