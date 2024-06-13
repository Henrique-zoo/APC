M = int(input())
A = int(input())
B = int(input())

if 110 >= M >= 40 and M > A >= 1 and M > B >= 1 and A != B:
    C =  M - A - B
    if C > B and C > A:
        print(C)
    elif B > C and B > A:
        print(B)
    elif A > C and A > B:
        print(A)