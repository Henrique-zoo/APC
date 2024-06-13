v, t = map(int, input().split())
trocas = [int(x) for x in input().split()]
volumeFinal = v
for vt in trocas:
    volumeFinal += vt
    if volumeFinal < 0:
        volumeFinal = 0
    if volumeFinal > 100:
        volumeFinal = 100
print(volumeFinal)