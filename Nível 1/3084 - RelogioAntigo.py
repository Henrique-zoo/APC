while True:
    try:
        h, m = map(int, input().split())
        horas = h // 30
        min = m // 6
        if horas < 10:
            horas = str(horas)
            horas = "0" + horas
        if min < 10:
            min = str(min)
            min = "0" + min
            
        print(f'{horas}:{min}')
    except EOFError:
        break