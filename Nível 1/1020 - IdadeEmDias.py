dias = int(input())

anos = dias // 365
resto = dias % 365
meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")