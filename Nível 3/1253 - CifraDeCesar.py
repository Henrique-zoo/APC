'''import dis'''


def decifrar(a, d):
    novaString = ''
    for i in range(0, len(a)):
        j = ord(a[i]) - d
        if j < 65:
            j += 26
        novaString += chr(j)
    print(novaString)
n = int(input())
while n > 0:
    n -= 1
    string = input()
    d = int(input())
    decifrar(string, d)
'''dis.dis(decifrar)'''