# coding: utf-8

# 1. feladat
print("1. feladat:")

tomb = []

with open("beosztas.txt") as file:
    for sor in file:

        beosztas = []

        # tanar
        sor = sor.strip()
        beosztas.append(sor)

        # tantargy
        sor = next(file).strip()
        beosztas.append(sor)

        # osztaly
        sor = next(file).strip()
        beosztas.append(sor)

        # oraszam
        sor = next(file).strip()
        beosztas.append(sor)

        tomb.append(beosztas)

    print(tomb)


# 2. feladat
print("2. feladat:")

bejegyzes = 0

for i in tomb:
    if int(i[3]) >= 0:
        bejegyzes = bejegyzes + 1

print("A fájlban " + str(bejegyzes) + " bejegyzés van.")


# 3. feladat
print("3. feladat:")

tanora = 0

for i in tomb:
    if int(i[3]) > 0:
        tanora = tanora + int(i[3])

print("Az iskolában a heti összóraszám: " + str(tanora))


# 4. feladat
print("4. feladat:")

tanarNeve = input("Adja meg egy tanár nevét! Egy tanár neve = ")

oraSzam = 0

for i in tomb:
    if str(i[0]) == str(tanarNeve):
        oraSzam = oraSzam + int(i[3])

print("A tanár heti óraszáma: " + str(oraSzam))


# 5. feladat
print("5. feladat:")

with open("of.txt", "w") as file:
    for beosztas in tomb:
        if str(beosztas[1]) == "osztalyfonoki":
            file.write(beosztas[2] + " - " + beosztas[0] + "\n")


# 6. feladat
print("6. feladat:")

print("Adja meg egy osztály és egy tantárgy nevét!")

osztaly = input("Osztály= ")

tantargy = input("Tantárgy= ")


# 7. feladat:
print("7. feladat:")

