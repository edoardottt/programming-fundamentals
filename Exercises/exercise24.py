#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:36:27 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
"""
Write a function that take as input a list of integers and edits it making sure
that it won't contain integers that are 3-multiple.
ATTENTION: It edits it, it doesn't create new one... 
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 18, 19, 21, 24, 26]


def edit_list_no_3(l):
    lista_remove = set()
    for i in range(len(l)):
        if l[i] % 3 == 0:
            lista_remove.add(l[i])
    for item in l:
        if item in lista_remove:
            l.remove(item)
    return l


# Version without range
def edit_list_no_3_2(l):
    lista_remove = set()
    for item in l:
        if item % 3 == 0:
            lista_remove.add(item)
    for item in l:
        if item in lista_remove:
            l.remove(item)
    return l


# Version with while
def edit_list_no_3_3(l):
    lista_remove = set()
    i = 0
    while i < len(l):
        if l[i] % 3 == 0:
            lista_remove.add(l[i])
    for item in l:
        if item in lista_remove:
            l.remove(item)
    return l
