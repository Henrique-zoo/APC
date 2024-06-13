id1, n1, preco1 = input().split()
id2, n2, preco2 = input().split()

id1 = int(id1)
id2 = int(id2)
n1 = int(n1)
n2 = int(n2)
preco1 = float(preco1)
preco2 = float(preco2)

precoTotal = preco1*n1 + preco2*n2

print(f'VALOR A PAGAR: R$ {precoTotal:.2f}')