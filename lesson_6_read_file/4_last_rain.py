# coding: utf-8

# Task #1: Read the data from the file.
# Task #2: Print the time of the earliest rain.
# Task #3: Print the time and location of the latest rain.


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

    print("Earliest rain today: " + min_time)

    # Task #3

    max_time = "0000"
    max_city = ""

    for rain in array:
        if int(max_time) < int(rain[1]):
            max_time = rain[1]
            max_city = rain[0]

    print("Location and time of last rain: " + max_city + ", "
          + max_time[0] + max_time[1] + ":" + max_time[2] + max_time[3])