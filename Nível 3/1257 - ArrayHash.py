def hash(a):
    n = ord(a) - 65
    return n
while True:
    try:
        x = int(input())
        while x > 0:
            x -= 1
            n = int(input())
            elemento = soma = 0
            while n > 0:
                n -= 1
                string = input()
                pos = ans = 0
                for i in string:
                    k = hash(i)
                    ans += k + pos + elemento
                    pos += 1
                elemento += 1
                soma += ans
            print(soma)
    except(EOFError):
        break