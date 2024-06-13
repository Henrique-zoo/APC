i = 0
ans = 0
soma = 0
while i < 6:
    i += 1
    x = float(input())
    if x > 0:
        ans += 1
        soma = x + soma
media = soma / ans
print(f'{ans} valores positivos\n{media:.1f}')