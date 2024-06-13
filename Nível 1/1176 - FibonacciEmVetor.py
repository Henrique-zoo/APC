t = int(input())
while t > 0:
    fibonacci = [0, 1]
    x = int(input())
    for i in range(2, x+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(f"Fib({x}) = {fibonacci[x]}")
    t -= 1