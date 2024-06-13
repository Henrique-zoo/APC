n = int(input())
inn = 0
out = 0

for _ in range(n):
    x = int(input())
    if 10 <= x <= 20:
        inn += 1
    else:
        out += 1
print(f'{inn} in\n{out} out')