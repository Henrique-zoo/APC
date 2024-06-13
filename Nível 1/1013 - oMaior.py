a, b, c = map(int, input().split())
maiorAB = (a + b + abs(a - b))/2
maiorGeral = int((maiorAB + c + abs(maiorAB - c))/2)

print(f'{maiorGeral} é o maior')