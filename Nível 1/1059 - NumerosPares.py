def contagem(a):
    if a > 0:
        contagem(a-2)
        print(a)
contagem(100)