A, B = map(float, input().split())

diferenca = abs(A - B)

aumento = diferenca/A*100

print(f'{aumento:.2f}%')