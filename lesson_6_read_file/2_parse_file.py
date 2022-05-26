# coding: utf-8

with open("data.txt") as file:
    for line in file:
        # removes whitespaces
        line = line.strip()

        # makes an array from a string
        line = line.split()

        city = line[0]
        time = line[1]
        wind = line[2]

        print(time)