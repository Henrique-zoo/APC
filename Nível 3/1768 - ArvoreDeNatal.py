while True:
    try:
        n = int(input())
        espacos = j = n//2
        for i in range(1, n+1, 2):
            print(espacos * " " + "*" * i)
            espacos -= 1
        for i in range(1, 4, 2):
            print(j * " " + "*" * i)
            j -= 1
        print()
    except(EOFError):
        break