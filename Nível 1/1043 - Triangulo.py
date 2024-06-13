A, B, C = map(float, input().split())

if A + B <= C or A + C <= B or B + C <= A:
    area = (A + B)/2 * C
    print(f"Area = {area:.1f}")
else:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")