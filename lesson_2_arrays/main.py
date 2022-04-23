#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Minden programodnak így kell kezdődnie.
if __name__ == '__main__':

    print("Tömb hossza:")

    # tömb hossza
    tomb = ["szo1", "szo2"]
    print(len(tomb))     # ezt irja ki: 2

    # a tömb első eleme
    print("Tömb első eleme: " + tomb[0])

    # a tömb második eleme
    print("Tömb második eleme: " + tomb[1])

    # a tömb utolsó eleme
    print("Tömb utolsó eleme: " + tomb[len(tomb)-1])

    # új elem hozzáadása a tömbhöz
    tomb.append("szo4")

    print("Tömb új értéke: " + str(tomb))


    # maradekos osztas
    print("Maradekos osztas")
    print(5 % 2)        # ezt irja ki: 1



    # for ciklus
    # tömb bejárása egyszerűen
    print("For ciklus:")

    for tomb_eleme in tomb:
        print(tomb_eleme)



    # Ha olyan nyert, aki nem tud főzni, akkor írd ki: "Aaa, gecibe!" !
    print("Damu feladat:")

    tudFozni = ["Roland", "Pincer az etteremben"]
    nemTudFozni = ["Gyozo", "Annacska", "Romeo"]

    nyertes = "Gyozo";

    if nyertes in nemTudFozni:
        print("Aaa, gecibe!")




    # számok kiiratása 0-tol 9-ig
    print("Számok kiirasa 0-tol 9-ig:")
    for x in range(0, 10):
        print(x)

    # páros számok kiiratása 0-tol 9-ig
    print("Páros szamok kiirasa:")
    for x in range(0, 10):
        if x % 2 == 0:
            print(x)


    # résztömb
    print("Tömb és indexek:")

    tomb = ["Andika", "Mate", "Doroti", "Dorci"]

    for index, value in enumerate(tomb):
        print("Ennyiedik elem: " + str(index))
        print("Hozzátartozó érték: " + value)
