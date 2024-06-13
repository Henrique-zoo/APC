D = int(input())

if D <= 800:
    pts = 1
elif D > 800 and D <= 1400:
    pts = 2
elif D > 1400 and D <= 2000:
    pts = 3
    
print(pts)