#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:05:27 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
"""
This function prints the sum of the numbers in a list.
"""


def sum_elements_list(lista):
    somma = 0
    for i in lista:
        if type(i) == int or type(i) == float:
            somma += i
    return somma
