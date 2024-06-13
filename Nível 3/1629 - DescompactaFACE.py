while True:
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        x = input()
        zeros = 0
        uns = 0
        for i in range(len(x)):
            if i % 2 == 0:
                zeros += int(x[i])
            else:
                uns += int(x[i])
        zeros = str(zeros)
        uns = str(uns)
        soma = 0
        for numero in zeros:
            soma += int(numero)
        for numero in uns:
            soma += int(numero)
        print(soma)