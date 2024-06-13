def areaLosango(n):
    if n > 0:
        x, y = map(int, input().split())
        area = int(x * y / 2)
        print(f'{area} cm2')
        areaLosango(n - 1)

n = int(input())
areaLosango(n)