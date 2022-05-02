# coding: utf-8

# 1. feladat: Olvassa be a fájl tartalmát!
# 2. feladat: Írja ki a legkorábbi eső időpontját!
# 3. feladat: Írja ki a legkésőbbi eső időpontját és helyét!


# 1. feladat
with open("szoveges_allomany.txt") as file:
    # 2. feladat
    print("2. feladat")
    minimalna = "2400"
    for sorocska in file:
        # kiszedi a felesleges spaceket és entereket
        sorocska = sorocska.strip()

        # a stringből tömböt csinál
        sorocska = sorocska.split()

        varos = sorocska[0]
        ido = sorocska[1]
        szel = sorocska[2]

        if int(minimalna) > int(ido):
            minimalna = ido

    print("A legelső eső ma: " + minimalna)


    # nagyon fontos:
    # ha egyszer végig mentünk a fájlon, akkor megint vissza kell tekerni az elejére
    # különben nem tudjuk majd megint bejárni
    file.seek(0)

    # 3. feladat
    print("3. feladat")
    maximum_ido = "0000"
    maximum_varosa = ""
    for sorocska in file:
        # kiszedi a felesleges spaceket és entereket
        sorocska = sorocska.strip()

        # a stringből tömböt csinál
        sorocska = sorocska.split()

        varos = sorocska[0]
        ido = sorocska[1]
        szel = sorocska[2]

        if int(maximum_ido) < int(ido):
            maximum_ido = ido
            maximum_varosa = varos

    print("A legutolsó eső helye és ideje: " + maximum_varosa + ", "
          + maximum_ido[0] + maximum_ido[1] + ":" + maximum_ido[2] + maximum_ido[3])