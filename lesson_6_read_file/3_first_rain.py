# coding: utf-8

# 1. feladat: Olvassa be a fájl tartalmát!
# 2. feladat: Írja ki a legkorábbi eső időpontját!


# 1. feladat
with open("szoveges_allomany.txt") as file:


    tomb = []

    for sorocska in file:
        # kiszedi a felesleges spaceket és entereket
        sorocska = sorocska.strip()

        # a stringből tömböt csinál
        sorocska = sorocska.split()

        tomb.append(sorocska)

    # 2. feladat
    print("2. feladat:")

    minimalna = "2400"
    for eso in tomb:
        if int(minimalna) > int(eso[1]):
            minimalna = eso[1]

    print("A legelső eső ma: " + minimalna)