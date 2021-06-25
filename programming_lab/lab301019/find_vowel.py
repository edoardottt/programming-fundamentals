#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 12:44:03 2019

@author: angelo
Write a function that takes a file name and returns the vowel that repeats the most times on the same line in the file. If there are vowels that are repeated the same number of times, the first one found returns.

ex:
    rotto
    topo
    missili

    returns i
"""


def find_vowel(filename):
    with open(filename) as f:
        maxvow = 0
        voc = ""
        for line in f:
            for vowel in "aeiou":
                cont = line.count(vowel)
                if cont > maxvoc:
                    voc = vowel
                    maxvoc = cont
    return voc


find_vowel("head_vowels.txt")
