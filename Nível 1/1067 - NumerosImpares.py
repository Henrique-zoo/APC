def impar(n):
    if n > 0:
        if n % 2 == 0:
            n = n - 1
        impar(n-2)
        print(n)
        
x = int(input())
impar(x)