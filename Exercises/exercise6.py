#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:05:27 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
'''
This function prints the sum of the numbers in a list.
2nd version
'''
def sum_elements_list2(lista):
    somma = 0
    for i in range(len(lista)):
        if type(lista[i])==int or type(lista[i])==float:
            somma += lista[i]
    return somma
