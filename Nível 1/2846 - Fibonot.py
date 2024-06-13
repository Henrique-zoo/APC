'''
def fib(n):
    fibonacci = [1,]
    a = 1
    b = 1
    for _ in range(n + 8):
        a, b = b, a + b
        fibonacci.append(a)
    return fibonacci
def naturais(n):
    naturais = [i for i in range(1, n + 10)]
    return naturais
def fibonot(fibonacci, naturais):
    fibonot = []
    for elemento in naturais:
        if elemento not in fibonacci:
            fibonot.append(elemento)
    return fibonot

K = int(input())
fibonacci = fib(K)
naturais = naturais(K)
fibonot = fibonot(fibonacci, naturais)
print(fibonot[K - 1])
'''