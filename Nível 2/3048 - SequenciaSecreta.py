n = int(input())
seq = []
j = k = x = 0
while n > 0:
    n-=1
    k = x
    x = int(input())
    if k != x:
        j += 1
print(j)