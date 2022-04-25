#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Minden programodnak így kell kezdodnie.
if __name__ == '__main__':

    ### Find max

    # We declare an array
    myArray = [4, 6, 1, 3, 8]

    # We declare a helper variable
    # We add a very small value for that
    max = 0

    # Our plan: iterate through the array
    for element in myArray:
        # we check if the current "element" is larger than the current "max" value
        if element > max:
            # if the "element" is larger than "max"
            # than it should be the new "max" value
            max = element

    # now let us check the final value of "max"
    print("Max of array: " + str(max))


    ### Keresd meg a legnagyobb 100 alatti értéket a tömbben!

    # We declare a helper variable
    # We add a very small value for that
    max = 0

    bigArray = [40, 26, 112, 434, 84]
    for element in bigArray:
        # we check if the current "element" is larger than the current "max" value
        # AND smaller than 100
        if element > max and element < 100:
            # if the "element" is larger than "max"
            # AND smaller than 100
            # than it should be the new "max" value
            max = element

    # now let us check the final value of "max"
    print("Largest element under 100: " + str(max))


    ### Find the smallest element of array

    # We declare a helper variable
    # We add a very big value for that
    min = 99999999

    numberArray = [5, 10, 11, 4, 8]
    for element in numberArray:
        # we check if the current "element" is larger than the current "max" value
        # AND smaller than 100
        if element < min:
            # if the "element" is larger than "max"
            # AND smaller than 100
            # than it should be the new "max" value
            min = element

    # now let us check the final value of "max"
    print("Min of array: " + str(min))