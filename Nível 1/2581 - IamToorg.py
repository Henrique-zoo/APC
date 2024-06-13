def resposta(n):
    if n > 0:
        question = input()
        print("I am Toorg!")
        resposta(n - 1)
        
x = int(input())
resposta(x)