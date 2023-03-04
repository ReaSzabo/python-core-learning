# coding: utf-8

age = raw_input("Welcome to the tobacco shop, how old are you? ")

# integer - whole number
# you can make integer from a string with the function "int()"
if int(age) > 18:
    print("Here is you cigarette. 1780Ft, please.")
else:
    print("You are not old enough. Please leave the shop.")
