#!/usr/bin/env python
# coding: utf-8

# Tt's boilerplate code that protects users from accidentally invoking the script when they didn't intend to
if __name__ == '__main__':

    # We use the print() command to print text to the terminal.
    print("Hello Andika")

    # In PyCharm you can run the scripts with the green triangle button.

    # The command lines do not need semicolon at the end.

    # We do not need "var" to declare a variable.

    text = "this is text"

    # Ese of "if"
    # 1. if keyword
    # 2. condition (without brace)
    # 3. colon
    # 4. the block is marked with a 4-space intention

    my_number = 4
    if my_number < 5:
        print("Small number")

    if my_number < 5 and my_number != 0:
        print("Small number and not zero")

    text = "This is a string"

    # boolean
    truth = True
    lie = False

    # array
    array = ["Gandalf", "Aragorn", "Theoden"]

    print("First element: " + array[0])

    for element in array:
        print("Actual element: " + element)

