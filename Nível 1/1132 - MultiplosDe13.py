def minemax(a, b):
    if a <= b:
        return a, b
    else:
        return b, a
sum = 0
x = int(input())
y = int(input())
x, y = minemax(x, y)
for i in range(x, y+1):
    if i % 13 != 0:
        sum += i
print(sum)