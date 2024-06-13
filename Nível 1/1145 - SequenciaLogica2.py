x, y = map(int, input().split())
for i in range(1, y, x):
    for j in range(i, i+x-1):
        print(j, end=" ")
    print(i+x-1)