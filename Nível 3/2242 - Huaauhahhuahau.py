risada = input()
vogais = ['a', 'e', 'i', 'o', 'u']
vogaisDaRisada = ''
vogaisDaRisadaInv = ''
for i in range(len(risada)):
    if risada[i] in vogais:
        vogaisDaRisada += risada[i]
for i in range(len(risada)-1, -1, -1):
    if risada[i] in vogais:
        vogaisDaRisadaInv += risada[i]
if vogaisDaRisada == vogaisDaRisadaInv:
    print('S')
else:
    print('N')