def criptografa(a):
    if (ord(a) >= ord('a') and ord(a) <= ord('z')) or (ord(a) >= ord('A') and ord(a) <= ord('Z')):
        return chr(ord(a) - 1)
    else:
        return a

k = int(input())
criptografada = ''
while k > 0:
    k -= 1
    string = input()
    for i in range(0, len(string)):
        c = criptografa(string[i])
    criptografada += c
    print(criptografada)