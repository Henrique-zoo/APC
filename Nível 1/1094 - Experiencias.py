n = int(input())
total = coelhos = ratos = sapos = 0
while n > 0:
    q, t = input().split()
    q = int(q)
    total += q
    if t == 'C':
        coelhos += q
    elif t == 'R':
        ratos += q
    elif t == 'S':
        sapos += q
    n -= 1
percentC = coelhos / total * 100
percentR = ratos / total * 100
percentS = sapos / total * 100

print(f'''Total: {total} cobaias
Total de coelhos: {coelhos}
Total de ratos: {ratos}
Total de sapos: {sapos}
Percentual de coelhos: {percentC:.2f} %
Percentual de ratos: {percentR:.2f} %
Percentual de sapos: {percentS:.2f} %''')