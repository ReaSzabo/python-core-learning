# coding: utf-8

array = ["doboz", "láda", "táska", "zsák", "batyu", "tarisznya", "puttony", "skatulya", "szelence", "Chanel"]

thing = raw_input("Kérem adja meg mibe akar pakolni: ")

if thing in array:
    print("Ebbe tud pakolni.")
else:
    print("Sajnálom, de ebbe nem tud pakolni. :(")
