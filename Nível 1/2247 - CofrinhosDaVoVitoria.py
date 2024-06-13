i = 1
n = int(input())
while n > 0:
    j = 1
    print(f"Teste {i}")
    dif = 0
    while j <= n:
        x, y = map(int, input().split())
        dif = x - y + dif
        print(f"{dif}")
        j += 1
    n = int(input())
    i += 1
    print()