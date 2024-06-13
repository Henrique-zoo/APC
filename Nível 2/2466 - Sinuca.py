n = int(input())
matriz = []

for _ in range(n):
    matriz.append([0]*n)
    
matriz[0] = [int(_) for _ in input().split()]

for i in range(1, n):
    for j in range(i, n):
        if matriz[i-1][j-1] == matriz[i-1][j]:
            matriz[i][j] = 1
        else:
            matriz[i][j] = -1
            
if matriz[n-1][n-1] == -1:
    print('branca')
else:
    print('preta')