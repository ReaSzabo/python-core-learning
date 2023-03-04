# coding: utf-8

# Egy tömbben adatokat tárolunk.
# A tömbünkben tömbök vannak.
# A kicsi tömböknek két eleme van.
# Az első egy város kódja, a második pedig a nap egy időpontja, amikor esett az eső.
# Az időpontok egy négyszámjegyes formátumban szerepelnek, amik az órát és percet jelentik.
# Pl "1812" -> 18:12 (18 óraa 12 perc).

rains = [
    ["Budapest", "0820"],
    ["Budapest", "1000"],
    ["Budapest", "1230"],
    ["Budapest", "0800"],
]

esett = False
varos = input("Adj meg egy várost: ")

for i in rains:
    if str(i[0]) == str(varos):
        if int(i[1]) > 1200:
            esett = True

if esett == True:
    print("A megadott városban esett az eső délután.")
else:
    print("A megadott városban nem esett az eső délután.")

