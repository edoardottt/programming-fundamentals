#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:26:08 2019

@author: angelo

Write a function that takes a string of words separated by input spaces and returns the set of distinct words. The string must also be cleansed of all punctuation marks (i.e. commas, periods, exclamation points, question marks, semicolons, colons, apostrophes, quotation marks)


example: "ciao ciao se beccamo" {"ciao","se","beccamo"}
"""


def distinct_words(string):
    s = set()
    string = string.replace("'", " ")
    for parola in string.split():
        word = word.strip(",.!?;:'\"")
        s.add(word)
    return s
