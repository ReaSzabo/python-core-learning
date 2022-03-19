# Minden programodnak igy kell kezdodnie.
if __name__ == '__main__':

    print("Tomb hossza:")

    # tomb hossza
    tomb = ["szo1", "szo2"]
    print(len(tomb))     # ezt irja ki: 2

    # hozzaadas a tombhoz
    tomb.append("szo4")

    print("Tomb uj erteke:" + str(tomb))


    # maradekos osztas
    print("Maradekos osztas")
    print(5 % 2)        # ezt irja ki: 1



    # for ciklus
    # tomb bejarasa egyszeruen
    print("For ciklus:")

    for elem in tomb:
        print(elem)



    # Ha olyan nyert, aki nem tud fozni, akkor ird ki: "Aaa, gecibe!" !
    print("Damu feladat:")

    tudFozni = ["Roland", "Pincer az etteremben"];
    nemTudFozni = ["Gyozo", "Annacska", "Romeo"];

    nyertes = "Gyozo";

    if nyertes in nemTudFozni:
        print("Aaa, gecibe!")




    # szamok kiiratasa 0-tol 9-ig
    print("Szamok kiirasa 0-tol 9-ig:")
    for x in range(0, 10):
        print(x)

    # paros szamok kiiratasa 0-tol 9-ig
    print("Paros szamok kiirasa:")
    for x in range(0, 10):
        if x % 2 == 0:
            print(x)
