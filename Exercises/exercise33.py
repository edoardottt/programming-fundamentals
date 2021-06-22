#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:37:03 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

"""
Write a function that take as input a list and it returns a new list containing 
tuples. Every tuples has as first element an element o9f the input and as
second element the count of that element.
es:
    [1,2,2,2,'b','a','a',2.0,2.0,2.0,'casa',2.0,'casa']
    [(1,1),(2,3),('b',1),('a',2),(2.0,4),('casa',2)]
"""

from random import randint

list1 = [1, 2, 2, 2, "b", "a", "a", 2.0, 2.0, 2.0, "casa", 2.0, "casa"]
list2 = [randint(0, 3000000) for _ in range(10000)]


def foo2(l):
    diz = {}
    for elem in l:
        if (elem, type(elem)) not in diz:
            diz[elem, type(elem)] = 1
        else:
            diz[elem, type(elem)] += 1
    return [(el[0], diz[el]) for el in diz]


print(foo2(list2))

# another version
def foo3(l):
    diz = {(elem, type(elem)): 0 for elem in l}
    for elem in l:
        diz[(elem, type(elem))] += 1
    return [(el[0], diz[el]) for el in diz]


print(foo2(list2))
