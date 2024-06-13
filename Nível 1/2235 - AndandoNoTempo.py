A, B, C = map(int, input().split())

pos1 = A + B - C
pos2 = A - B - C
pos3 = A - B + C
pos4 = B - A - C
pos5 = A - B
pos6 = A - C
pos7 = B - C

if pos1 * pos2 * pos3 * pos4 * pos5 * pos6 * pos7 == 0:
    print("S")
else:
    print("N")