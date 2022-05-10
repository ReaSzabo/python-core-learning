# coding: utf-8

# Create a file and write the content of an array into it
array = ["kecske", "kutya", "macska"]
with open("my_file_2.txt", 'w') as file:
    for animal in array:
        # Enter (new line) is marked as "\n" in programming
        file.write(animal + "\n")
