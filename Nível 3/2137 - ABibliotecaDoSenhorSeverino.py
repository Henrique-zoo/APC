while True:
    try:
        n = int(input())
        codigos = []
        for _ in range(n):
            codigos.append(input())
        for i in range(len(codigos)):
            for j in range(i+1, len(codigos)):
                if codigos[j] < codigos[i]:
                    aux = codigos[i]
                    codigos[i] = codigos[j]
                    codigos[j] = aux
        for codigo in codigos:
            print(codigo)
    except EOFError:
        break