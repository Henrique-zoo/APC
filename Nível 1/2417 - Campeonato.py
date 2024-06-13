Cv, Ce, Cs, Fv, Fe, Fs = map(int, input().split())

Cpontos = Cv * 3 + Ce
Fpontos = Fv * 3 + Fe

if Cpontos > Fpontos:
    print("C")
elif Fpontos > Cpontos:
    print("F")
else:
    if Cs > Fs:
        print("C")
    elif Fs > Cs:
        print("F")
    else:
        print("=")