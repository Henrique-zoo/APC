soma = j = 0
while True:
    n = float(input())
    if n < 0 or n > 10:
        print("nota invalida")
    else:
        soma += n
        j += 1
    if j == 2:
        break
media = soma / j
print(f"media = {media:.2f}")