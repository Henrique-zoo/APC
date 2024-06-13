n1, n2, n3, n4 = map(float, input().split())

media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 7.0 and media >= 5:
    n5 = float(input())
    media = (media + n5)/2
    print("Aluno em exame.")
    print(f"Nota do exame: {n5:.1f}")
    if media >= 5:
        print("Aluno aprovado.")
    else: 
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
else:
    print("Aluno reprovado.")