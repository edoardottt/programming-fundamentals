#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 17:49:25 2019

@author: angelo
Write a function that takes a string that is the name of a file, and returns the vowel that occurs multiple times on the same line of the file

Ex: if the file contains
 buffo
 pope
 richiami

 return 'i'
"""


def maximum_vowel(filename):
    ripvoc = 0
    voc = ""
    with open(filename) as f:
        for line in f:
            for v in "aeiou":
                cont = line.count(v)
                if cont > ripvoc:
                    ripvoc = cont
                    voc = v
    return voc
