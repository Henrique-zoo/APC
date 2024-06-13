n = int(input())
ans = 0
while n > 0:
    n -= 1
    a, b = input().split()
    x = 0
    for i in range(0, len(a)):
        k = ord(b[i])
        j = ord(a[i])
        if k >= j:
            x += k - j
        else:
            x += ord('z') - j + 1 + (k - ord('a'))
    print(x)