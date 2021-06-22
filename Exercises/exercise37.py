#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:22:30 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input something and verify if it's a valid matrix.
"""


def check_matrix(m):
    if type(m) != list:
        return False
    if len(m) == 0 or type(m[0]) != list:
        return False
    colonne = len(m[0])
    for riga in m:
        if type(riga) != list or len(riga) != colonne:
            return False
        for el in riga:
            if not isinstance(el, (int, float)):
                return False
    return True
