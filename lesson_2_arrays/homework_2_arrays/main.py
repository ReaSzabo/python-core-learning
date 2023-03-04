#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Minden programodnak így kell kezdődnie.
if __name__ == '__main__':
    # Írd ki a tömb hosszát!
    array1 = [1, 2, 3, 4, 5]

    print(len(array1))



    # Írd ki a tömb első elemét!
    array2 = [1, 2, 3, 4, 5]

    print(array2[0])



    # Írd ki a tömb utolsó elemét!
    array3 = [1, 2, 3, 4, 5]

    print(array3[len(array3)-1])



    # Írd ki a nagyobbik (több elemű) tömb méretét!
    # (Ne ránézésre mondd meg, hogy melyik a hosszabb, hanem if-fel vizsgáld meg!)
    array4 = [1, 3, 5, 6, 7]
    array5 = [4, 6, 7]

    if len(array4) > len(array5):
        print("A nagyobb tömb hossza " + str(len(array4)))
    else:
        print("A nagyobb tömb hossza " + str(len(array5)))



    # A kisebbik (kevesebb elemű) tömbhoz add hozzá a 100-as számot! (Legyen az is a tömb eleme)
    array6 = [1, 3, 5, 6, 7]
    array7 = [4, 6, 7]

    if len(array6) < len(array7):
        array6.append(100)
    else:
        array7.append(100)






    # For ciklussal írd ki a számokat 5-tol 10-ig


    for i in range(1, 6):
        print(i)

