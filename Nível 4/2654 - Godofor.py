n = int(input())
pMaior = kMaior = mMenor = lMaior =0
nomeMaior = ''
for _ in range(n):
    nome, p, k, m = input().split()
    p = int(p); k = int(k); m = int(m)
    if p > pMaior:
        pMaior = p
        kMaior = k
        mMenor = m
        nomeMaior = nome
        lMaior = len(nome)
    elif p == pMaior:
        if k > kMaior:
            pMaior = p
            kMaior = k
            mMenor = m
            nomeMaior = nome
            lMaior = len(nome)
        elif k == kMaior:
            if m < mMenor:
                pMaior = p
                kMaior = k
                mMenor = m
                nomeMaior = nome
                lMaior = len(nome)
            elif m == mMenor:
                if len(nome) < lMaior:
                    pMaior = p
                    kMaior = k
                    mMenor = m
                    nomeMaior = nome
                    lMaior = len(nome)
print(nomeMaior)