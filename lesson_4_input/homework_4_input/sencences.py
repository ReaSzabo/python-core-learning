# coding: utf-8

# Python tanulmányaid legnagyobb kihívásához érkeztél.
# Szorgalmi feladat. Ugyanilyen van az érettségiben.

# Nézzünk meg egy tömböt, amiben tömbök vannak.
# A nagyobb tömb a mondatok halmaza. A kis tömbök pedig az egyes mondatok szavait tartalmazzák.

mondatok = [
    ["Szia", "Andi"],
    ["Mate", "vagyok"],
    ["Hogy", "vagy"]
]

# Hogy járhatjuk be az mondatok halmazát?
for mondat in mondatok:
    print(mondat) # Kiírja az egyes mondatokat tömbként. Pl. ["Szia", "Andi"]

print("Első szavak:")
# Hogyan írhatjuk ki minden mondat első szavát?
for mondat in mondatok:
    print(mondat[0]) # Kiírja a mondatok első szavát stringként. Pl. "Szia"

print("Második szavak:")
# Hogyan írhatjuk ki minden mondat második szavát?
for mondat in mondatok:
    print(mondat[1]) # Kiírja a mondatok második szavát stringként. Pl. "Andi"

# Képzeljünk el egy helyzetet, amikor az első szót megvizsgáljuk if-fel, és ha teljesül a feltétel, akkor kiírjuk a másodikat.
print("Feltétel:")
for mondat in mondatok:
    if mondat[0] == 'Szia':
        print(mondat[1])

# Na most, a feladatod az, hogy kérj be egy szót a felhasználótól.
# Ha a bekért szó a mondat első szavával megegyezik, akkor írd ki a mondat második szavát.
# Pl, ha a bekért szó "Hogy", akkor írd ki "vagy".
# Nem baj, ha nem sikerül, elég nehéz a feladat!!!!!

print("Bekéréses feladat:")

bekertSzo = input("Adjál meg egy szót ide neh: ")

for mondat in mondatok:
    if str(bekertSzo) == mondat[0]:
        print(mondat[1])
