# coding: utf-8

# Kérj be egy számot és vizsgáld meg, hogy páros-e vagy páratlan.
# Írd ki, hogy "páratlan szám" vagy "páros szám".
# Pl, ha a bekért szám 10, írd ki "páros szám"

bekertSzam = input("Adj meg egy számot, te süket: ")
if int(bekertSzam) % 2 == 0:
    print("Ez a szám páros.")
else:
    print("Ez a szám páratlan.")