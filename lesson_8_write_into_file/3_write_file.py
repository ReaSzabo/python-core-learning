# coding: utf-8

# Create files by files for each animal.
array = ["horse", "dog", "cat"]
for animal in array:
    with open(animal + ".txt", 'w') as file:
        file.write("This file was created to pay respect for " + animal + "!!!")
