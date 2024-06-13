n = int(input())
for _ in range(n):
    strings = input().split(' ')
    decifrado = ''
    for string in strings:
        if string != '':
            decifrado += string[0]
    print(decifrado)