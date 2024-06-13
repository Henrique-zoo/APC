while True:
    x1, y1, x2, y2 = map(int, input().split())
    
    if x1 == x2 == y1 == y2 == 0:
        break
    elif y1 == y2 and x1 == x2:
        print(0)
    elif (x1 != x2 and y1 == y2) or (x1 == x2 and y1 != y2):
        print(1)
    elif (y2 - y1)/(x2 - x1) == 1 or (y2 - y1)/(x2 - x1) == -1:
        print(1)
    else:
        print(2)