def somandoIndice(a, iEntreAspas, separador):
    j = 0
    indices = []
    for i in range(len(a)):
        if a[i] == separador:
            j += 1
        if j > 0:
            for k in range(j):
                i += iEntreAspas[k] - 1
        indices.append(i)
    return indices
def criandoString(a, b):
    aspas = [i for i in range(len(a)) if a[i] == '"']
    substring = ''
    if len(aspas) > 1:
        for i in range(aspas[0], aspas[1] + 1):
            substring += a[i]
        b.append(len(substring))
        string = a.replace(substring, "$")
        return criandoString(string, b)
    return a, b
def limpandoEspacos(a, iEntreAspas):
    string = f'{a[0]}'
    indices = []
    indices2 = []
    largura = []
    for i in range(1, len(a)):
        if a[i] == " " and a[i-1] == " ":
            indices.append(iEntreAspas[i])
            indices2.append(iEntreAspas[i])
        else:
            largura.append(len(indices2))
            string += a[i]
    return string, indices, largura
def informal(a, iEntreAspas):
    indices = []
    palavras = a.split()
    j = 0
    for palavra in palavras:
        for i in range(1, len(palavra)):
            if (65 <= ord(palavra[0]) <= 122 and 48 <= ord(palavra[i]) <= 57) or (48 <= ord(palavra[0]) <= 57 and 65 <= ord(palavra[i]) <= 122):
                indices.append(iEntreAspas[i+j])
        j += len(palavra) + 1
    return indices
def maiusculo(a, iEntreAspas):
    indices = []
    for i in range(1, len(a)-1):
        if 65 <= ord(a[i]) <= 90 and (65 <= ord(a[i-1]) <= 122 or a[i-2] != "."):
            indices.append(iEntreAspas[i])
    return indices
def minusculo(a, iEntreAspas):
    indices = []
    if 97 <= ord(a[0]) <= 122:
        indices.append(0)
    for i in range(len(a)-1):
        if a[i] == '.' and (122 > ord(a[i+2]) > 97):
            indices.append(iEntreAspas[i+2])
    return indices
def pontuacao(a, iEntreAspas):
    indices = []
    for i in range(len(a)-1):
        if a[i] in {'.', ',', '"'} and (a[i-1] == ' ' or 65 <= ord(a[i+1]) <= 90 or 97 <= ord(a[i+1]) <= 122):
            indices.append(iEntreAspas[i])
    return indices

texto = input()
largura = []
texto, largura = criandoString(texto, largura)
indiceEntreAspas = somandoIndice(texto, largura, "$")
texto, espacos, largura = limpandoEspacos(texto, indiceEntreAspas)
for i in range(len(largura)):
    if indiceEntreAspas[i] >= i:
        indiceEntreAspas[i] += largura[i]
inf = informal(texto, indiceEntreAspas)
mai = maiusculo(texto, indiceEntreAspas)
min = minusculo(texto, indiceEntreAspas)
pont = pontuacao(texto, indiceEntreAspas)
if espacos == inf == mai == min == pont == []:
    print("SIM")
else:
    print("NAO")
    if espacos != []:
        print(f'ESPACO EM BRANCO')
        print(*espacos)
    if inf != []:
        print("INFORMAL")
        print(*inf)
    if mai != []:
        print(f'MAIUSCULA')
        print(*mai)
    if min != []:
        print(f'MINUSCULA')
        print(*min)
    if pont != []:
        print(f"PONTUACAO")
        print(*pont)