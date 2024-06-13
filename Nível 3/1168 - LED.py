n = int(input())
qtdPerNumero = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}
while n > 0:
    numero = input()
    leds = 0
    for i in numero:
        leds += qtdPerNumero[i]
    print(f"{leds} leds")
    n -= 1