def calculaSalario(descricao, pontoDeFeno):
    salario = 0
    for palavra in descricao.split():
        if palavra in pontoDeFeno:
            salario += pontoDeFeno[palavra]
    return salario

m, n = map(int, input().split())

pontoDeFeno = {}
for _ in range(m):
    palavra, valor = input().split()
    pontoDeFeno[palavra] = int(valor)

for _ in range(n):
    descricao = ""
    linha = input()
    while linha != ".":
        descricao += linha + " "
        linha = input().strip()
    salario = calculaSalario(descricao, pontoDeFeno)
    
    print(salario)