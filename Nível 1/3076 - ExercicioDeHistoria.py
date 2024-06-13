while True:
    try:
        ano = int(input())
        sec = int(ano / 100 + 0.99)
        print(sec)
    except EOFError:
        break