#!/usr/bin/env python
# coding: utf-8

if __name__ == '__main__':

    print("Length of array:")

    # length of an array
    array = ["word1", "word2"]
    print(len(array))

    # first element of array
    print("First element of array: " + array[0])

    # second element of array
    print("Second element of array: " + array[1])

    # last element of array
    print("Last element of array: " + array[len(array)-1])

    # add element to an array
    array.append("word4")

    print("New value of array: " + str(array))


    # division with remainder
    print("division with remainder")
    print(5 % 2)



    # for loop
    # iterate through array
    print("For loop:")

    for array_element in array:
        print(array_element)


    # Fun example
    # Ha olyan nyert, aki nem tud főzni, akkor írd ki: "Aaa, gecibe!" !
    print("Damu exercise:")

    can_cook = ["Roland", "Pincer az etteremben"]
    cannot_cook = ["Gyozo", "Annacska", "Romeo"]

    winner = "Gyozo"

    if winner in cannot_cook:
        print("Aaa, gecibe!")




    # numbers from 0 to 9
    print("Numbers from 0 to 9: ")
    for x in range(0, 10):
        print(x)

    # even numbers from 0 to 9
    print("Even numbers:")
    for x in range(0, 10):
        if x % 2 == 0:
            print(x)
