L, C, X, Y = map(int, input().split())

if C % 2 == 0:
    if Y % 2 != 0:
        print("Esquerda")
    else:
        print("Direita")
else:
    if (X + Y) % 2 == 0 or X + Y == 0:
        print("Direita")
    else:
        print("Esquerda")