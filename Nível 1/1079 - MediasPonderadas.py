n = int(input())
while n > 0:
    n -= 1
    x, y, z = map(float, input().split())
    media = (2 * x + 3 * y + 5 * z)/10
    print(f'{media:.1f}')