n = int(input())
while n > 0:
    n -= 1
    x = int(input())
    if x % 2 == 0 and x != 0:
        print("EVEN", end=' ')
    elif x == 0:
        print('NULL', end='\n')
    elif x % 2 != 0:
        print("ODD", end=' ')
    if x > 0:
        print("POSITIVE", end='\n')
    if x < 0:
        print("NEGATIVE", end='\n')