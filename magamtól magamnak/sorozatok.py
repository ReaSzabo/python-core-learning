# coding: utf-8

# 1. feladat

tomb = []

with open("lista.txt") as file:
    for sor in file:

        epizod = []

        # datum
        sor = sor.strip()
        epizod.append(sor)

        # neve
        sor = next(file).strip()
        epizod.append(sor)

        # evad
        sor = next(file).strip()
        epizod.append(sor)

        # hossz
        sor = next(file).strip()
        epizod.append(sor)

        # latta
        sor = next(file).strip()
        epizod.append(sor)

        tomb.append(epizod)

# 2. feladat
print("2. feladat:")

szamlalo = 0

for i in tomb:
    if str(i[0]) != "NI":
        szamlalo = szamlalo + 1

print("A listában " + str(szamlalo) + " db vetítési dátummal rendelkező epizód van.")


# 3. feladat
print("3. feladat:")

osszes = 0

for i in tomb:
    if int(i[4]) == 0 or 1:
        osszes = osszes + 1

megnezett = 0

for i in tomb:
    if int(i[4]) == 1:
        megnezett = megnezett + 1

szazalekosan = megnezett / osszes

print("A listában lévő epizódok " + str(szazalekosan)[2] + str(szazalekosan)[3] + "," + str(szazalekosan)[4] + str(szazalekosan)[5] + "%-át látta.")


# 4.feladat
print("4. feladat:")

eltoltottIdo = 0

for i in tomb:
    if int(i[4]) == 1:
        eltoltottIdo = eltoltottIdo + int(i[3])

napSzamitas = (eltoltottIdo / 60) / 24
nap = str(napSzamitas)[0]
oraSzamitas = (eltoltottIdo / 60) - (int(nap) * 24)
ora = str(oraSzamitas)[0:2]
napOra = (int(nap) * 24) * 60 + (int(ora) * 60)
perc = eltoltottIdo - napOra

print("Sorozatnézéssel " + str(nap) + " napot " + str(ora) + " órát " + str(perc) + " percet töltött.")

# 5. feladat
print("5.feladat:")

datum = input("Adjon meg egy dátumot! Dátum = ")

for i in tomb:
    if str(i[0]) <= str(datum):
        if int(i[4]) == 0:
            print(str(i[2]) + "\t" + str(i[1]))







