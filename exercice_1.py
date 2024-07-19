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

def filter_positive_numbers(numbers):

    """
    Détecte les nombres négatifs dans la liste (intrus).
    Détecte les nombres positifs dans la liste et les afficher.
    :param numbers: Liste de nombres
    :return: Liste des nombres négatifs et/ou positifs.
    """

    negative_numbers = [num for num in numbers if num < 0]

    for num in numbers:
        if num < 0:
            break
    else:
        print("No intruder number detected in the list.")

    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:
        print(positive_numbers)

numbers = input_list_numbers()
filter_positive_numbers(numbers)
