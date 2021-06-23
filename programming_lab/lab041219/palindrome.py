#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:00:44 2019

@author: angelo

Write a palindrome recursive function that takes a string as input and returns True if it is a palindrome, False otherwise

oro anna osso aveva ossesso ottetto
itopinonavevanonipoti

Base code: a letter -> True
           two letters -> True if the two letters are the same

case recursive: word[0] == word[-1] and palindrome (word[1:-1])

codice OPIS : BGFZSJXL

"""


def palindrome(word):
    if len(word) <= 1:
        return True
    return word[0] == word[-1] and palindrome(word[1:-1])
