# coding: utf-8

array = []
with open("szoveges_allomany.txt") as file:
    for sor in file:

        epizod = []

        # datum
        sor = sor.strip()
        epizod.append(sor)

        # sorozat neve
        sor = next(file).strip()
        epizod.append(sor)

        # aktualis resz
        sor = next(file).strip()
        epizod.append(sor)

        # hossz
        sor = next(file).strip()
        epizod.append(sor)

        # megnezte-e
        sor = next(file).strip()
        epizod.append(sor)

        array.append(epizod)

    print(array)