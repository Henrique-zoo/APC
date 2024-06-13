i = 1
n = int(input())
while n > 0:
    j = 1
    print(f"Teste {i}")
    dif = 0
    while j <= n:
        x, y = map(int, input().split())
        dif = x - y + dif
        j += 1
    if dif > 0:
        print("Aldo")
    else:
        print("Beto")
    n = int(input())
    i += 1
    print()