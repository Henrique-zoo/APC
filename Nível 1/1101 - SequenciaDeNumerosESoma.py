def minemax(a, b):
    if a >= b:
        return b, a
    else:
        return a, b
    
while True:
    n, m = map(int, input().split())
    n, m = minemax(n, m)
    if n <= 0 or m <= 0:
        break
    sum = 0
    for i in range(n, m+1):
        print(f'{i}', end=" ")
        sum += i
    print(f'Sum={sum}')