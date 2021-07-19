#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:49:01 2019

@author: angelo
"""


def get_numbers():
    """The function continuously fetches a string from the keyboard, if the string is a number then it prints its square on the screen, otherwise it does nothing. Exits the function when the user enters the word "done" and returns the number of squares calculated."""
    square_count = 0
    string = ""
    while string != "fine":
        string = input("Enter the string")
        if string.isnumeric():
            print(int(string) ** 2)
            square_count = square_count + 1
    return square_count
