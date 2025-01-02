N = int(input())

if N <= 10:
    conta = 7
elif N > 10 and N <= 30:
    conta = 7 + N - 10
elif N > 30 and N <= 100:
    conta = 7 + 20 + (N - 30)*2
elif N > 100:
    conta = 7 + 20 + 140 + (N - 100)*5

print(conta)