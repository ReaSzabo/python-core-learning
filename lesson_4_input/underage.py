# coding: utf-8

age = raw_input("Üdvözlöm én egy dohánybolti eladó vagyok. Kérem mondja meg hány éves: ")

# integer - egész szám
# stringből egész számot csinálni: int()
if int(age) > 18:
    print("Itt a cigi! 1760 Ft lesz.")
else:
    print("Te nem vagy 18... Legyél szíves fáradj ki az üzlethelyiségből!")
