#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function that takes as argument a string containing a series of words (sequences of characters separated by whitespace, tabs or carriage returns) and an integer and returns the number of words in the string that have a length exactly equal to the integer taken as subject
example: word_count("a e i o u", 1) returns 5
         word_count("asd bip casa", 3) returns 2
         word_count('ciao
                  pippo



                  pluto', 4) returns 1
"""


def word_count(string, length):
    list = string.split()
    c = 0
    for word in list:
        if len(word) == length:
            c = c + 1
    return c
