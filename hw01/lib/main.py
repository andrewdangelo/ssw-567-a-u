# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:05:00 2021

This file contains the code necessary for the attainment of full credit on the triangle classification assignment

@author: Andrew D'Angelo
"""


def classify_triangle(a: int, b: int, c: int):

    # Equilateral - all sides equal
    # Isosceles - 2 sides equal
    # Scalene - No sides equal
    # Right - a^2 + b^2 = c^2

    if a == b and b == c:
        return "Equilateral"
    
    elif a == b or b == c:
        return "Isosceles"

    elif a != b and b != c  and a != c and a**2 + b**2 != c**2:
        return "Scalene"

    elif a**2 + b**2 == c**2:
        return "Right"

    else:
        return "Invalid"


def run_classify(a: int, b: int, c: int):
    triangle = classify_triangle(a,b,c)
    print(f'{triangle} triangle')




