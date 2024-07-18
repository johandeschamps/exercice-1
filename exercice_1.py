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

# ----------------------------------------------

for num in numbers:
    if num < 0:
        print(f"The first intruder detected is : {num}")
        break
else:
    print("No intruder detected in the list.")

