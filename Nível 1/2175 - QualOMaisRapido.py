def maisRapido(a, b, c):
    if a < b and a < c:
        return "Otavio"
    elif b < a  and b < c:
        return "Bruno"
    elif c < a and c < b:
        return "Ian"
    else:
        return "Empate"
o, b, i = map(float, input().split())
print(maisRapido(o, b, i))