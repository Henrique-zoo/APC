A, B, C = map(float, input().split())
delta = B ** 2 - (4 * A * C)

if delta <= 0 or A == 0:
    print("Impossivel calcular")
else:
    bhaskara1 = (-B + delta**(1/2))/(2*A)
    bhaskara2 = (-B - delta**(1/2))/(2*A)
    print(f'R1 = {bhaskara1:.5f}\nR2 = {bhaskara2:.5f}')