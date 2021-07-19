#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:42:28 2019

@author: angelo
"""


def vowel_counts():
    """The function continuously takes a string from the keyboard until the user enters the letter 'z' and returns the number of inserted strings corresponding to vowels (regardless of capitalization)"""
    counter = 0
    s = ""
    while s != "z":
        s = input("Enter the string: ")
        if s in "aeiouAEIOU" and len(s) == 1:
            counter = counter + 1
    return counter
