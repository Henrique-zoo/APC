n = int(input())
for _ in range(n):
    n1, n2 = map(int, input().split())
    n3 = str(n1**n2)
    print(len(n3))