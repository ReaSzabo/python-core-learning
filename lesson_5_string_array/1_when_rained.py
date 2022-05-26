# coding: utf-8


# We contain data in an array.
# The array contains arrays.
# The small arrays has 2 elements, information about rains in the country.
# The first element is a city name and the second one is the time of rain.
# The time is a 4-digits string. They are the hours and minutes in 2-digis format.
# Pl "1812" -> 18:12 (18 hours 12 minutes).

rains = [
    ["Budapest", "0800"],
    ["Budapest", "0820"],
    ["Budapest", "1000"],
    ["Budapest", "1230"],
    ["Budapest", "1730"],
    ["Budapest", "1920"],
    ["Debrecen", "0920"],
    ["Debrecen", "1020"],
    ["Debrecen", "1115"],
    ["Debrecen", "1900"],
    ["Szeged", "0600"],
    ["Szeged", "0700"],
    ["Szeged", "0800"],
    ["Miskolc", "0800"],
    ["Miskolc", "0920"],
    ["Miskolc", "1920"],

]

# Get a time code from the user and see where it was raining that time.

time = input("Please add a time: ")
for rain in rains:
    if rain[1] == time:
        print(rain[0])
