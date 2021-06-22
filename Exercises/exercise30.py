# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 19:36:00 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a dictionary having as keys a string
and as values an integer.
The f has to return a list containing all the kesy having an even value
sorted.
For example -->
{ ’topolino’:12, ’pluto’:3, ’minnie’:7, ’pippo’:4, ’qui’:3 }
la funzione deve restituire la lista [’pippo’,’topolino’].
"""


def foo(d):
    result = [k for k in d.keys() if d[k] % 2 == 0]
    return sorted(result)
