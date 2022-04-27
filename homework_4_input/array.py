# coding: utf-8

# Írd ki a tömb azon elemeit, amelyek nagyobbak, mint a bekért szám!
# Természetesen be kell kérned ezt a számot a felhasználótól.
# Pl, ha a a bekért szám 99, akkor írd ki:
# 100
# 200
nagySzamok = [100, 49, 10, 55, 200]

bekertSzam = input("Adj meg egy számot: ")
for i in nagySzamok:
    if i > int(bekertSzam):
        print(i)
