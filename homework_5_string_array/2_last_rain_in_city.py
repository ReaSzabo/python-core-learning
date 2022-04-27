# coding: utf-8

# Egy tömbben adatokat tárolunk.
# A tömbünkben tömbök vannak.
# A kicsi tömböknek két eleme van.
# Az első egy város kódja, a második pedig a nap egy időpontja, amikor esett az eső.
# Az időpontok egy négyszámjegyes formátumban szerepelnek, amik az órát és percet jelentik.
# Pl "1812" -> 18:12 (18 óraa 12 perc).

rains = [
    ["Budapest", "0800"],
    ["Budapest", "0820"],
    ["Budapest", "1000"],
    ["Budapest", "1230"],
    ["Budapest", "1730"],
    ["Budapest", "1920"],
    ["Debrecen", "0920"],
    ["Debrecen", "1020"],
    ["Debrecen", "1115"],
    ["Debrecen", "1900"],
    ["Szeged", "0600"],
    ["Szeged", "0700"],
    ["Szeged", "0800"],
    ["Miskolc", "0800"],
    ["Miskolc", "0920"],
    ["Miskolc", "1920"],

]

# Kérj be egy várost a felhasználótól és add meg, mikor volt a legutolsó eső ott!
# Pl. input -> "Debrecen", output -> "1900"
