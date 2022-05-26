# coding: utf-8

array = ["box", "bad", "handbag", "suitcase", "pouch", "luggage", "package"]

thing = input("What do you want to pack in? ")

if thing in array:
    print("You can pack in it.")
else:
    print("Unfortunately you cannot pack in it. :(")
