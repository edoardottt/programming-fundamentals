# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:12:24 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Write a function that take as input a dictionary and returns the inverted
dict. So the keys of the result will have the values as keys, and as values
the keys that have that values as values in input.
'''

def foo(d):
    diz = {}
    for item in d.values():
        l = [key for key in d.keys() if d[key] == item]
        diz[item] = l
    return diz