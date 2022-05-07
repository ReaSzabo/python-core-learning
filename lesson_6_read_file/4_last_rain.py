# coding: utf-8

# 1. feladat: Olvassa be a fájl tartalmát!
# 2. feladat: Írja ki a legkorábbi eső időpontját!
# 3. feladat: Írja ki a legkésőbbi eső időpontját és helyét!


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

    # 3. feladat
    print("3. feladat")

    maximum_ido = "0000"
    maximum_varosa = ""

    for eso in tomb:
        if int(maximum_ido) < int(eso[1]):
            maximum_ido = eso[1]
            maximum_varosa = eso[0]

    print("A legutolsó eső helye és ideje: " + maximum_varosa + ", "
          + maximum_ido[0] + maximum_ido[1] + ":" + maximum_ido[2] + maximum_ido[3])