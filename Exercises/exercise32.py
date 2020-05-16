# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:52:58 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

'''
Write a function that take as input two dictionaries (key:list) and 
returns a new dict. having as keys only the keys that are in both dictionaries
and as values the union of the two values of that keys.
'''

def foo(d1,d2):
    return {k:d1[k]+d2[k] for k in d1.keys() if k in d2}