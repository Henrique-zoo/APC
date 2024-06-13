while True:
    h1, m1, h2, m2 = map(int, input().split())
    if m1 == m2 == h1 == h2 == 0:
        break
    mi = h1 * 60 + m1
    if h2 < h1 or (h1 == h2 and m2 < m1):
        h2 = h2 + 24
    mf = h2 * 60 + m2
    mdormidos = mf - mi
    print(mdormidos)