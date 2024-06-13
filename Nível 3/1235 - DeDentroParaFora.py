n = int(input())
for _ in range(n):
    string = input()
    stringCorreta = ''
    meio = (len(string) // 2) - 1
    for i in range(meio, -1, -1):
        stringCorreta += string[i]
    for i in range(len(string)-1, meio, -1):
        stringCorreta += string[i]
    print(stringCorreta)