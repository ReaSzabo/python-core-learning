# coding: utf-8

# 1. feladat

with open("utasadat.txt") as file:

    tomb = []

    for sor in file:
        sor = sor.strip()
        sor = sor.split()

        tomb.append(sor)

# 2. feladat
print("2. feladat:")

szamlalo = 0

for i in tomb:
    if int(i[0]) >= 0:
        szamlalo = szamlalo + 1

print("A buszra " + str(szamlalo) + " utas szeretett volna felszállni.")

# 3. feladat
print("3. feladat:")

utasJegy = 0

for i in tomb:
    if str(i[3]) == "JGY":
        if int(i[4]) == 0:
            utasJegy = utasJegy + 1

utasBerlet = 0

for i in tomb:
    datum = i[1]
    if str(i[3]) != "JGY":
        if str(datum[0:8]) > str(i[4]):
            utasBerlet = utasBerlet + 1

utas = utasJegy + utasBerlet

print("A buszra " + str(utas) + " utas nem szállhatott fel.")


# 4. feladat
print("4. feladat:")




# 5. feladat
print("5.feladat")

kedvezmenyes= 0
ingyenes = 0


ervenyesseg = (i[1])

for i in tomb:
    if str(i[3]) == "TAB" or str(i[3]) == "NYB":
        if str(ervenyesseg[0:8]) <= str(i[4]):
            kedvezmenyes = kedvezmenyes + 1

for i in tomb:
    if str(i[3]) == "NYP" or str(i[3]) == "RVS" or str(i[3]) == "GYK":
        if str(ervenyesseg[0:9]) <= str(i[4]):
            ingyenes = ingyenes + 1

print("Ingyenesen utazók száma: " + str(ingyenes) + " fő")
print("A kedvezményesen utazók száma: " + str(kedvezmenyes) + " fő")








