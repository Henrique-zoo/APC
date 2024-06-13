while True:
    try:
        string = input()
        stringFinal = ''
        j = 0
        for letra in string:
            a = ord(letra)
            if letra != ' ':
                if j % 2 == 0 and 97 <= a <= 122:
                    a -= 32
                elif j % 2 == 1 and 65 <= a <= 90:
                    a += 32
                j += 1
            stringFinal += chr(a)
        print(stringFinal)
    except EOFError:
        break