v = input()
m = input()
o = input()

if v == "vertebrado":
    if m == "ave":
        if o == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if o == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if m == "inseto":
        if o == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if o == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")