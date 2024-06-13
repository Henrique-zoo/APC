n = int(input())
for _ in range(n):
    string = input()
    a = int(string[0])
    letra = string[1]
    b = int(string[2])
    if a == b:
        resposta = int(a)**2
    elif 65 <= ord(letra) <= 90:
        resposta = b - a
    elif 97 <= ord(letra) <= 122:
        resposta =  a + b
    print(resposta)