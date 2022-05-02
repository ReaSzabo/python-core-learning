# coding: utf-8

# 1. feladat: Olvassa be a fájl tartalmát!
# 2. feladat: Írja ki a legkorábbi eső időpontját!


# 1. feladat
with open("szoveges_allomany.txt") as file:
    # 2. feladat
    print("2. feladat:")
    minimalna = "0000"
    for sorocska in file:
        # kiszedi a felesleges spaceket és entereket
        sorocska = sorocska.strip()

        # a stringből tömböt csinál
        sorocska = sorocska.split()

        varos = sorocska[0]
        ido = sorocska[1]
        szel = sorocska[2]

        if int(minimalna) < int(ido):
            minimalna = ido

    print("A legelső eső ma: " + minimalna)