n = int(input())
for _ in range(n):
    t, l = map(int, input().split())
    traducao = {}
    for _ in range(t):
        japones = input()
        portugues = input()
        traducao[japones] = portugues
    for _ in range(l):
        letra = input().split()
        string = ''
        for i in range(len(letra)):
            if letra[i] in traducao:
                if i != len(letra) - 1:
                    string += traducao[letra[i]] + ' '
                else:
                    string += traducao[letra[i]]
            else:
                if i != len(letra) - 1:
                    string += letra[i] + ' '
                else:
                    string += letra[i]
        print(string)
    print()