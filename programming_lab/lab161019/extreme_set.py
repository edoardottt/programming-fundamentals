#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:28:14 2019

@author: angelo

Write a function that takes as argument a list of integers and two integers and returns the set of elements between the two integers taken as parameters that are present in the list.

example [56, 12, 8, 100] 5,15 {8,12}
"""
def extreme_set(list, a, b):
    s = set()
    for el in list:
        if a <= el <=b:
            s.add(el)
    return s

def extreme_set2(list, a, b):
    s = set(list)
    extreme = set(range(a,b+1))
    return s & extreme



def count(list, extremea, extremeb):
    s = set()
    for el in lista:
        if extremea < el < extremeb:
            s.add(el)
    return s


def count2(list, extremea, extremeb):
    s = set()
    array = set(lista)
    for el in range(extremea, extremeb+1):
        if el in array:
            s.add(el)
    return s

def count3(list, extremea, extremeb):
    array = set(lista)
    extremes = set(range(extremea, extremeb+1))
    return array.intersection(extremes)

def count4(list, extremea, extremeb):
    s = set()
    array = set(list)
    i = extremea
    while i < extremeb:
        if i in array:
            s.add(i)
        i+=1
    return s

def count5(list, extremea, extremeb):
    s = set()
    i = extremea
    while i < extremeb:
        if i in list:
            s.add(i)
        i+=1
    return s
