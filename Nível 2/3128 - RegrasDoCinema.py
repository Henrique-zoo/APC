x = int(input())
y = int(input())
lista = [x, y]
[a, b] = sorted(lista)

if a >=14 and b >= 14:
    print("YES")
elif a < 18:
    if b >= 18 and a >= 6:
        print("YES")
    else:
        print("NO")