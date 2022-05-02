# coding: utf-8

with open("szoveges_allomany.txt") as file:
    for sorocska in file:
        # kiszedi a felesleges spaceket és entereket
        sorocska = sorocska.strip()

        # a stringből tömböt csinál
        sorocska = sorocska.split()

        varos = sorocska[0]
        ido = sorocska[1]
        szel = sorocska[2]

        print(sorocska)
