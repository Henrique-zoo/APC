i = 0
ans = 0
while i < 5:
    i += 1
    x = float(input())
    if x % 2 == 0:
        ans += 1
print(f'{ans} valores pares')