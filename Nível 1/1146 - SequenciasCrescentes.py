while True:
    x = int(input())
    if x == 0:
        break
    for i in range(1, x):
        print(i, end=" ")
    print(x)