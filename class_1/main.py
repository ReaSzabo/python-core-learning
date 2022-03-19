# Minden programodnak igy kell kezdodnie.
if __name__ == '__main__':

    # nem console.log() van, hanem print()
    print("Szia Andika")

    # lefuttatni a programot a zold haromszoggel lehet fent

    # a parancsok vegere nem kell pontosvesszo

    # valtozo deklaralashoz nem kell "var"

    # if hasznalata
    # 1. if keyword
    # 2. feltetel, de zarojelek nelkul (csak space kell a feltetel es az if koze)
    # 3. kettospont
    # 4. a vegrehajtando blokknak 4 szokozzel beljebb kell kerulnie

    szam = 4
    if szam < 5:
        print("Kis szam")

    if szam < 5 and szam != 0:
        print("Nem nulla es kicsi")

    szoveg = "Ez egy string"

    # A boolean ertekeket nagy betuvel kezdjuk
    igazsag = True
    hazugsag = False

    # tomb
    tomb = [1, 3, 5]

    print("Elso elem: " + str(tomb[0]))

    for elemke in tomb:
        print("Az elemem: " + str(elemke) )

    # object
    objektum = {
        "nev": "Andi"
    }

    print(objektum)
    print(objektum['nev'])
