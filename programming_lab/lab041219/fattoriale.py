#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:27:57 2019

@author: angelo

6!
6*5*4*3*2*1 = 6 * 5!
5! 5*4*3*2*1 = 5 * 4!
...
1! = 1

n! = n * (n-1)!

"""


def fattoriale(n):
    if n == 1:
        return 1
    return n * fattoriale(n - 1)


def fattoriale_iterativo(n):
    fatt = 1
    for i in range(n, 1, -1):
        fatt *= i
    return fatt
