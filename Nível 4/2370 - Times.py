times = {}
jogadores = {}
n, t = map(int, input().split())
for _ in range(n):
    nome, overall = input().split()
    overall = int(overall)
    jogadores[overall] = nome
    
time_id = 1
overall_ordenado = sorted(jogadores, reverse = True)

for i in range(1, t+1):
    times[i] = []
for over in overall_ordenado:
    times[time_id].append(jogadores[over])
    time_id += 1
    if time_id > t:
        time_id = 1
for i in range(1, t+1):
    times[i].sort()
    print(f"Time {i}")
    for elemento in times[i]:
        print(elemento)
    print()