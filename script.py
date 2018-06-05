#!/usr/binpython3

import random


a = 10

b= 5

print(a + b)

#Ceci est un commentaire sur une ligne


def exo9():
    val = int(input("entrez un nombre :"))
    somme = 0
    for i in range(0, val+1):
        somme = i + somme
    print(somme)
'''
14 Si nous listons tous les nombres naturels inférieurs à 10 qui sont des multiples de 3 et 5, nous avons 3, 5, 6 et 9. La somme de ces multiples est 23.
Trouvez la somme de tous les multiples de 3 et 5 inférieurs à 1000. 

'''
