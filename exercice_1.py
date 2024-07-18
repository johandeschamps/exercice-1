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
        print(f"The first intruder number detected is : {num}")
        break
else:
    print("No intruder number detected in the list.")

# ----------------------------------------------

negative_numbers = [num for num in numbers if num < 0]

if negative_numbers:
    print(f"Intruded number(s) detected : {negative_numbers}")
    print(f"Total number of intruded number(s) : {len(negative_numbers)}")

