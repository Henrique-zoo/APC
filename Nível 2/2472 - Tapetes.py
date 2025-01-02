L, N = map(int, input().split())

if L != N:
    M = L - (N - 1)
    A = M*M + (N-1)*1
else:
    A = 1*N
print(A)