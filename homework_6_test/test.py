# coding: utf-8

# 1. feladat
with open("tavirathu13.txt") as file:

    tomb = []

    for sor in file:
        sor = sor.strip()
        sor = sor.split()

        tomb.append(sor)

# 2. feladat
print("2. feladat:")

telepules = input("Adja meg egy település kódját! Település: ")

maximum = 0000

for i in tomb:
    if str(i[0]) == str(telepules):
        if int(i[1]) > int(maximum):
            maximum = i[1]

print("Az utolsó mérési adat a megadott településről " + maximum[0] + maximum [1] + ":" + maximum[2] + maximum[3] + "-kor érkezett.")


# 3. feladat
print("3. feladat:")

minimumFok = 50
minimumVaros = ""
minimumIdo = ""
maximumFok = 0
maximumVaros = ""
maximumIdo = ""

for i in tomb:
    if int(i[3]) < int(minimumFok):
        minimumFok = i[3]
        minimumVaros = i[0]
        minimumIdo = i[1]

for i in tomb:
    if int(i[3]) > int(maximumFok):
        maximumFok = i[3]
        maximumVaros = i[0]
        maximumIdo = i[1]

print("A legalacsonyabb hőmérséklet: " + minimumVaros + " " + minimumIdo[0] + minimumIdo[1] + ":" + minimumIdo[2] + minimumIdo[3] + " " + minimumFok + " " + "fok.")
print("A legmagasabb hőmérséklet: " + maximumVaros + " " + maximumIdo[0] + maximumIdo[1] + ":" + maximumIdo[2] + maximumIdo[3] + " " + maximumFok + " " + "fok.")


# 4. feladat
print("4. feladat:")

ido = ""

voltSzel = False

for i in tomb:
    if str(i[2]) == "00000":
        ido = i[1]
        voltSzel = True
        print(i[0] + " " + ido[0] + ido[1] + ":" + ido[2] + ido[3])

if voltSzel == False:
    print("Nem volt szélcsend a mérések idején.")




