C, Q = map(int, input().split())

class Comida:
    def __init__(self, id, preco):
        self.id = id
        self.preco = preco
    
    def __str__(self):
        return f"{self.id}({self.preco})"
    
HotDog = Comida(1, 4.00)
XSalada = Comida(2, 4.50)
XBacon = Comida(3, 5.00)
Torrada = Comida(4, 2.00)
Refri = Comida(5, 1.50)

if C == 1:
    item = HotDog
elif C == 2:
    item = XSalada
elif C == 3:
    item = XBacon
elif C == 4:
    item = Torrada
elif C == 5:
    item = Refri
else:
    item = None

if item is not None:
    valor_total = item.preco * Q
    print(f"Total: R${valor_total:.2f}")
