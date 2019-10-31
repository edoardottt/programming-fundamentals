#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:32:47 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Write a function that take as input a filename and returns the vocal most
repeated in the file for every line.
ex: If the file contains:
buffo
papa
richiami

result = 'i'
'''

def foo(n):
    massimo = ('a',0)
    with open(n) as f:
        s = f.readlines()
        for line in s:
            a = bar(line)
            if a[1] > massimo[1]:
                massimo = a
    return massimo
            
def bar(p):
    massimo = ('a',0)
    for item in 'aeiou':
        c = p.replace('',' ').split()
        if c.count(item) > massimo[1]:
            massimo = (item,c.count(item))
    return massimo