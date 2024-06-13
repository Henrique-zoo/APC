n = int(input())
ans = 0
while n > 0:
    n -= 1
    c, t = map(int, input().split())
    ans += c/t
if ans <= 1:
    print("OK")
else:
    print("FAIL")