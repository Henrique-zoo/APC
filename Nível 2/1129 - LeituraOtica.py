n = int(input())
while n != 0:
    alternativas = {}
    chaves = ['A', 'B', 'C', 'D', 'E']
    for i in range(n):
        pretoOuBranco = [int(x) for x in input().split()]
        for i in range(len(pretoOuBranco)):
            alternativas[chaves[i]] = pretoOuBranco[i]
        repetidas = 0
        for chave in alternativas:
            if alternativas[chave] <= 127:
                repetidas += 1
                ans = chave
        if repetidas >= 2 or repetidas == 0:
            print('*')
        else:
            print(ans)
    n = int(input())