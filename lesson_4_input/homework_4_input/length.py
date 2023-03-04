# coding: utf-8

# Ha a tanuló vonalzója 10 cm alatti, akkor írd ki: "Csepp", egyébként "Jó lesz."
# Kérd be a vonalzó hosszát egy length változóba.

# Pl, ha a bekért szám 11, akkor írd ki "Jó lesz"

length = input("Add meg a vonalzód hosszát: ")
if int(length) < 10:
    print("Csepp")
else:
    print("Jó lesz.")
