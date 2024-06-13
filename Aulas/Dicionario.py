'''
Dicionários:
    É uma estrutura de dados em que os elementos são armazenados e alterados por meio de uma chave (a chave é o índice da estrutura).
        ↪ A chave não precisa ser um número inteiro, ou seja, os índices não são necessariamente ordenados.
        ↪ As chaves são únicas, isto é, não podem ser repetidas
    Para cada chave, temos um objeto associado denominado valor. Esse objeto pode ser um int, string, uma lista e até outro dicionário.
'''
x = input()
dicionario = {
#Chaves  #Valores
    'A': 65,
    'B': 66,
    'C': 67,
    'D': 68
}

print(f"A chave '{x}' tem valor {dicionario[x]}")