# coding: utf-8

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

# Check when it was raining the first in the country.

min_time = "2400"
for rain in rains:
    if int(rain[1]) < int(min_time):
        min_time = rain[1]

print(min_time)
