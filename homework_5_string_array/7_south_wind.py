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
    ["Debrecen", "0800", "dél"],
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

# Írd ki, az összes esetet, amikor déli szél volt! Tudasd, hogy hol és mikor történt!
# Pl. "Debrecen 08:00-kor déli szél volt".

# Hogy tudjuk kiírni szépen az időpontokat:
#ido = "0800"
#varos = "Debrecen"
#print(varos + " " + ido[0] + ido[1] + ':' + ido[2] + ido[3] + " déli szél volt")
# Ez csak help, kitörölheted :)


for i in rains:
    if i[2] == "dél":
        varos = i[0]
        ido = i[1]
        print(varos + " " + ido[0] + ido[1] + ":"  + ido[2] + ido [3] + "-kor déli szél volt.")