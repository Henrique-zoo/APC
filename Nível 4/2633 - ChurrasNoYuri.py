while True:
    try:
        carnes = {}
        n = int(input())
        for _ in range(n):
            carne, validade = input().split()
            validade = int(validade)
            carnes[validade] = carne
        validadeEmOrdem = sorted(carnes)
        string = ''
        for validade in validadeEmOrdem:
            string += carnes[validade] + ' '
        print(string.strip())
    except EOFError:
        break