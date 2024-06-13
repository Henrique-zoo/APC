n = int(input())
mercado ={}
for _ in range(n):
    m = int(input())
    for _ in range(m):
        fruta, preco = input().split()
        preco = float(preco)
        mercado[fruta] = preco
    p = int(input())
    gasto = 0
    for _ in range(p):
        compra, qtd = input().split()
        qtd = int(qtd)
        if compra in mercado:
            gasto += mercado[compra]*qtd
    print(f'R$ {gasto:.2f}')