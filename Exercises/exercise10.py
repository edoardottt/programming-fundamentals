#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:05:54 2019

@author: edoardottt
"""

def conta_vocali():
    '''
    The function keep taking as input from keyboard a string until the
    user enters the character 'z' and it returns the vocals number 
    (it counts both vocals with uppercase and lowercase)
    '''
    num_vocali = 0
    stringa = ''
    while stringa != 'z':
        stringa = input("Inserisci una stringa: ")
        if stringa.lower() in "aeiou" and len(stringa)==1:
            num_vocali += 1
    return num_vocali
print(conta_vocali())