#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Minden programodnak így kell kezdődnie.
if __name__ == '__main__':
    # Keresd meg a legnagyobb 10 alatti értéket a tömbben!

    array1 = [4, 6, 8, 9, 10, 13]
    max = 0

    for elem in array1:
        if elem > max and elem < 10:
            max = elem

    print(max)


    ### Keresd meg a legkisebb 100 feletti érteket a tömbben!

    array2 = [30, 70, 90, 110, 150, 170]
    min = 1000

    for legkisebb in array2:
        if legkisebb < min and legkisebb > 100:
            min = legkisebb


    print(min)
