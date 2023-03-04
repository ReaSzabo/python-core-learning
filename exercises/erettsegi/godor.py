# coding: utf-8

# 1. feladat:
print("1. feladat:")

tomb = []

with open("melyseg.txt") as file:
    for sor in file:
        tomb.append(sor)

szamlalo = 0

for i in tomb:
    if int(i[0]) >= 0:
        szamlalo = szamlalo + 1

print("A fájl adatainak száma: " + str(szamlalo))


# 2. feladat
print("2. feladat:")

tavolsag = input("Adjon meg egy távolságértéket! ")

print("Ezen a helyen a felszín " + tomb[int(tavolsag) - 1] + " méter mélyen van.")


# 3. feladat
print("3. feladat")

erintetlen = 0
osszes = szamlalo


for i in tomb:
    if int(i) == 0:
        erintetlen = erintetlen + 1

szazalek = (erintetlen / osszes) * 100
print("Az érintetlen területek aránya: " + str(szazalek)[0:5] + "%.")


# 4. feladat

with open("godrok.txt", "w") as file:
    file.write()


# 5. feladat
print("5. feladat")


# 6. feladat
print("6. feladat:")

for i in tomb:
    if int(tomb[int(tavolsag) - 1]) == 0:
        print("Az adott helyen nincs gödör.")
    else:
        print("A gödör kezdete: ")
        if


