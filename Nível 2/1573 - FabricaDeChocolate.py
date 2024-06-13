import math


while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    else:
        volume = a*b*c
        aresta = math.floor((volume)**(1/3))
        print(aresta)