count = 0
while True:
    n = int(input())
    if n == 0:
        break
    if count != 0:
        print()
    maiorLargura = 0
    strings = []
    while n > 0:
        n -= 1
        string = input()
        strings.append(string)
        if len(string) > maiorLargura:
            maiorLargura = len(string)
    for string in strings:
        espaco = maiorLargura - len(string)
        print(f'{espaco * " "}{string}')
    count += 1