def maisDeOitoMil(c):
    if c > 0:
        e = int(input())
        if e > 8000:
            print("Mais de 8000!")
        else:
            print("Inseto!")
        maisDeOitoMil(c - 1)
        
c = int(input())
maisDeOitoMil(c)