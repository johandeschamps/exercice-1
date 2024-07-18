#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Exercice 1 Base Python
"""

numbers = []
while True:
    try:
        number = int(input("Enter number "))
        if number == 0:
            break
        numbers.append(number)
    except ValueError:
        print("Sorry, the input is not correct")
