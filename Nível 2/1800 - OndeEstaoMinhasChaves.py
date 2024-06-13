q, e = map(int, input().split())
eJaVisitados = input().split()
dicionario = {}
for si in eJaVisitados:
    dicionario[si] = '1'
for _ in range(q):
    ci = input()
    if ci in dicionario:
        print('0')
    else:
        print('1')
        dicionario[ci] = '1'