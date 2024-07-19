#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercice 1 Base Python
"""

# L'utilisateur rentre un nombre, Si le nombre saisi est égale à 0
# l'utilisateur sort de la boucle
# Sinon il ajoute le nombre à la liste "numbers".

numbers = []
while True:
    try:
        number = int(input("Enter number, 0 to exit : "))
        if number == 0:
            break
        numbers.append(number)
    except ValueError:
        print("Sorry, the input is not correct")

# Après avoir collecté les nombres, le code vérifie s’il y a des nombres négatifs
# dans la liste “numbers”, il itère à travers chaque nombre dans la liste.

for num in numbers:
    if num < 0:
        print(f"The first intruder number detected is : {num}")
        break
else:
    print("No intruder number detected in the list.")

# La liste appelée negative_numbers contient tous les nombres négatifs de
# la liste numbers d’origine (s’il y en a).

negative_numbers = [num for num in numbers if num < 0]

if negative_numbers:
    print(f"Intruded number(s) detected : {negative_numbers}")
    print(f"Total number of intruded number(s) : {len(negative_numbers)}")

# La liste appelée positive_numbers contient tous
# les nombres positifs de la liste numbers d’origine et l’affiche.

positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)

# ----------------------------------------------------------------------------
