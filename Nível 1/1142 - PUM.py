n = int(input())
j = 1
while n > 0:
    for i in range(j, j+3):
        print(i, end =" ")
    j += 4
    print("PUM")
    n -= 1