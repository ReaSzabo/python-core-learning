# coding: utf-8

# Egy tömbben adatokat tárolunk.
# A tömbünkben tömbök vannak.
# A kicsi tömböknek három eleme van.
# Az első egy város kódja, a második pedig a nap egy időpontja, amikor esett az eső.
# Az időpontok egy négyszámjegyes formátumban szerepelnek, amik az órát és percet jelentik.
# Pl "1812" -> 18:12 (18 óraa 12 perc).
# A harmadik elem pedig a szél iránya.
# Ha a szél iránya helyén a "NA" szerepel, akkor nem fújt a szél.

rains = [
    ["Budapest", "0800", "kelet"],
    ["Budapest", "0820", "észak"],
    ["Budapest", "1000", "kelet"],
    ["Budapest", "1230", "nyugat"],
    ["Budapest", "1730", "kelet"],
    ["Budapest", "1920", "nyugat"],
    ["Debrecen", "0800", "NA"],
    ["Debrecen", "0920", "észak"],
    ["Debrecen", "1020", "nyugat"],
    ["Debrecen", "1115", "kelet"],
    ["Debrecen", "1900", "dél"],
    ["Szeged", "0600", "észak"],
    ["Szeged", "0700", "kelet"],
    ["Szeged", "0800", "dél"],
    ["Miskolc", "0800", "kelet"],
    ["Miskolc", "0920", "észak"],

]

# Kérj be egy várost a felhasználótól és írd ki, hogy 08:00-kor milyen irányú szél fújt!
# Pl. input -> "Debrecen", output -> "dél"
# Ha nem fújt a szél, akkor a szélirány helyett írd ki: "Nem fújt a szél.".

varos = input("Adj meg egy várost: ")

szel = "NA"

for i in rains:
    if str(i[0]) == str(varos):
        if int(i[1]) == 800:
            szel = str(i[2])

if szel != str("NA"):
    print(szel)
else:
    print("Nem fújt a szél")

