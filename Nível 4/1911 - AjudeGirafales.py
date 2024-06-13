n = int(input())
while n != 0:
    assinaturasCorretas = {}
    presenca = {}
    for _ in range(n):
        nome, assinatura = input().split()
        assinaturasCorretas[nome] = assinatura
    m = int(input())
    count = 0
    for _ in range(m):
        nome, assinatura = input().split()
        erros = 0
        for i in range(len(assinatura)):
            if assinatura[i] != assinaturasCorretas[nome][i]:
                erros += 1
        if erros > 1:
            count += 1
    print(count)
    n = int(input())