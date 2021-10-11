#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:25:57 2019

@author: angelo

Write a function that takes a text file name as input and returns a dictionary of the frequencies of letters repeated consecutively in words.
Each line of the file must be considered as a single word, that is, the spaces that divide the characters of the same line must be ignored. 
The dictionary keys are the repeated letters and the values are the number of times the letter is repeated consecutively in the string.

example: the example.txt file contains

casa a amalfi
azione estremizzata
ripasso organizzato
eeeeeeeeeeeeeeeee ee e e e
aabaabaabaa


the resulting dictionary will be:
    {'a':5, 'e':2, 'z':2, 's':1, 'o':1}
"""


def repeated_frequencies(fname):
    dic = {}
    with open(fname) as f:
        for row in f:
            final = ""
            row = row.replace(" ", "")
            for index, character in enumerate(row[:-1]):
                if character == row[index + 1]:
                    if character != final:
                        dic[character] = dic.get(character, 0) + 1
                        final = character
                else:
                    final = character
    return dic
