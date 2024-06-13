x, y, z = map(int, input().split())

if x > y:
    if x > z:
        if y > z:
            print(z)
            print(y)
        else:
            print(y)
            print(z)
        print(x)
    else:
        print(y)
        print(x)
        print(z)
elif y > z:
    if x > z:
        print(z)
        print(x)
    else:
        print(x)
        print(z)
    print(y)
else:
    print(x)
    print(y)
    print(z)
print(f"\n{x}\n{y}\n{z}")