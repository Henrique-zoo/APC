def maior_com_indice(a, b, indice_a, indice_b):
    if a > b:
        return a, indice_a
    else:
        return b, indice_b

y = int(input())
maior_numero, indice_maior = y, 1

for i in range(2, 101):
    x = int(input())
    maior_numero, indice_maior = maior_com_indice(x, maior_numero, i, indice_maior)

print(f"{maior_numero}\n{indice_maior}")
