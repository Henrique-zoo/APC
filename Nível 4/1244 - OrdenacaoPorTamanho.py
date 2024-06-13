c = int(input())
for _ in range(c):
    stringFinal = ""
    dicionario = {}
    string = input().split()
    count = 1
    for palavra in string:
        if len(palavra) in dicionario:
            dicionario[len(palavra) - 0.01*count] = palavra
            count += 1
        else:
            dicionario[len(palavra)] = palavra
    tamanhos = sorted(dicionario, reverse = True)
    ultimo = len(tamanhos) - 1
    for i in range(0, len(tamanhos)- 1):
        stringFinal += dicionario[tamanhos[i]] + " "
    stringFinal += dicionario[tamanhos[ultimo]]
    print(stringFinal)