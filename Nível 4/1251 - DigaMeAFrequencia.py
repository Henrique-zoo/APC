while True:
    try:
        frequencia = {}
        string = input()
        for letra in string:
            if letra in frequencia:
                frequencia[ord(letra)] += 1
            else:
                frequencia[ord(letra)] = 1
        inv = {}
        for chave in frequencia:
            valor = frequencia[chave]
            if valor in inv:
                inv[valor].append(chave)
            else:
                inv[valor] = chave
    
    except EOFError:
        break