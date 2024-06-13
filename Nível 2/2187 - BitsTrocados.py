notas = [50, 10, 5]
i = 0
while True:
    i+=1
    v = int(input())
    if v == 0:
        break
    print(f"Teste {i}")
    for nota in notas:
        qnt = v // nota
        v = v % nota
        print(qnt, end=' ')
    print(f'{v}\n')