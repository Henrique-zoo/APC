n = int(input())
for _ in range(n):
    pessoas = int(input())
    idioma1 = input()
    diferentes = False
    for _ in range(pessoas - 1):
        idioma = input()
        if idioma != idioma1:
            diferentes = True
    if diferentes:
        print('ingles')
    else:
        print(idioma1)