def tipoDeTriangulo(a, b, c):
    if b > a:
        if b > c:
            aux = b
            b = a
            a = aux
        if c > a:
            aux = c
            c = a
            a = aux
    if a >= b + c:
        print("Invalido")
    else:
        if b == c and a == b:
            print("Valido-Equilatero")
        elif b == c or a == b or a == c:
            print("Valido-Isoceles")
        else:
            print("Valido-Escaleno")
            
        if a**2 == b**2 + c**2:
            print("Retangulo: S")
        else:
            print("Retangulo: N")
        
x, y, z = map(int, input().split())
tipoDeTriangulo(x, y, z)