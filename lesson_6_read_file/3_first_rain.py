# coding: utf-8

# Task #1: Read the data from the file.
# Task #2: Print the earliest rain.


# 1. feladat
with open("data.txt") as file:


    # Task #1

    array = []

    for line in file:
        line = line.strip()
        line = line.split()
        array.append(line)

    # Task #2

    min_time = "2400"
    for rain in array:
        if int(min_time) > int(rain[1]):
            min_time = rain[1]

    print("First rain today: " + min_time)