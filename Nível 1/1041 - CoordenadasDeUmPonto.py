x, y = map(float, input().split())

if y > 0:
    if x > 0:
        print("Q1")
    elif x < 0:
        print("Q2")
    else:
        print("Eixo Y")
elif y < 0:
    if x > 0:
        print("Q4")
    elif x < 0:
        print("Q3")
    else:
        print("Eixo Y")
else:
    if x != 0:
        print("Eixo X")
    else:
        print("Origem")