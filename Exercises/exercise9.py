#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:17:16 2019

@author: edoardottt
"""
def prendi_numeri():
    '''
    The function keep taking as input from keyboard a string until the user
    enters 'fine'. If the input is a number it prints the square root
    of that number. When it finish, it has to print the count of numbers printed.
    '''
    num_quadrati = 0
    stringa  = ''
    while stringa != 'fine':
        stringa  = input("Insert input: ")
        if stringa.isnumeric():
            num = int(stringa)
            print(num**2)
            num_quadrati+=1
        else:
            print("I take only numbers")
            print("Numbers printed: {}".format(num_quadrati))
            return num_quadrati
    return num_quadrati