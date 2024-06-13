B = int(input())
T = int(input())

areaNota = 70 * 160
areaTrapezio = (B + T)/2 * 70
if areaTrapezio > areaNota - areaTrapezio:
    print("1")
elif areaTrapezio == areaNota - areaTrapezio:
    print("0")
else:
    print("2")