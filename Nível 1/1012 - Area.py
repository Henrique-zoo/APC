A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
# Triângulo
areaTriangulo = A*C/2
# Círculo
pi = 3.14159
areaCirculo = pi*C**2
# Trapézio
areaTrapezio = (A+B)/2 * C
# Quadrado
areaQuadrado = B**2
# Retângulo 
areaRetangulo = A*B

print(f'TRIANGULO: {areaTriangulo:.3f}\nCIRCULO: {areaCirculo:.3f}\nTRAPEZIO: {areaTrapezio:.3f}\nQUADRADO: {areaQuadrado:.3f}\nRETANGULO: {areaRetangulo:.3f}')