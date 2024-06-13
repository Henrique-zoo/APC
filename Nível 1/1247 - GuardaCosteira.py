while True:
    try:
        d, vf, vg = map(int, input().split())

        dg = (d**2 + 12**2)**(1/2)
        tempoCosteira = dg / vg
        tempoLadrao = 12 / vf

        if tempoCosteira <= tempoLadrao:
            print('S')
        else:
            print('N')
    except EOFError:
        break