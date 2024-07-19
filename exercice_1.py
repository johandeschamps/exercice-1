#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercice 1 Base Python
"""

def input_list_numbers():

    """
    Invite l'utilisateur à rentrer un nombre, Si le nombre saisi est égale à 0
    l'utilisateur sort de la boucle. Sinon, il ajoute le nombre à la liste "numbers".
    :return: Liste des nombres saisis
    """

    numbers = []
    while True:
        try:
            number = int(input("Enter number, 0 to exit : "))
            if number == 0:
                break
            numbers.append(number)
        except ValueError:
            print("Sorry, the input is not correct")
    return numbers

def detect_numbers_intruder(numbers):

    """
    Détecte les nombres négatifs dans la liste (intrus) et les afficher.
    Détecte les nombres positifs dans la liste et les afficher.
    :param numbers: Liste de nombres
    :return: Liste des nombres négatifs et/ou positifs.
    """

    negative_numbers = [num for num in numbers if num < 0]

    for num in numbers:
        if num < 0:
            print(f"The first intruder number detected is : {num}")
            break
    else:
        print("No intruder number detected in the list.")

    if negative_numbers:
        print(f"Intruded number(s) detected : {negative_numbers}")
        print(f"Total number of intruded number(s) : {len(negative_numbers)}")

    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:
        print(positive_numbers)

numbers = input_list_numbers()
detect_numbers_intruder(numbers)
