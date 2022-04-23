#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Minden programodnak így kell kezdődnie.
if __name__ == '__main__':

    # nem console.log() van, hanem print()
    print("Szia Andika")

    # lefuttatni a programot a zöld haromszoggel lehet fent

    # a parancsok vegere nem kell pontosvessző

    # változó deklaráláshoz nem kell "var"

    szoveg = "szövegke"

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
    tomb = ["Teodor", "Sanyika", "Bilbó"]

    print("Elso elem: " + tomb[0])

    for elemke in tomb:
        print("Az aktuális elem: " + elemke)

    # object
    szemely = {
        "nev": "Andi",
        "kor": 27,
        "szep": True
    }

    print(szemely)
    print("A személy neve: " + szemely['nev'])

    butor = {
        "tipus": "szék",
        "labak": 4,
        "muanyag": False
    }

    print(butor)
    # a lábat számmal adtuk meg, viszont a plusz jellel egy stringhez próbáljuk hozzákötni
    # a str(...) függvénnyel bármi stringgé alakítható
    print("A bútor lábainak száma: " + str(butor['labak']))

