A, B, C = map(float, input().split())

if B > A:
    if B > C:
        aux = B
        B = A
        A = aux
if C > A:
    aux = C
    C = A
    A = aux
if A < B + C:
    if A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO RETANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or C == B:
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")