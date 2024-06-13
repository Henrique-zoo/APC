p = int(input())
digitosTotais = 0
for i in range(1, p+1):
    pag = str(i)
    digitos = len(pag)
    digitosTotais += digitos
print(digitosTotais)