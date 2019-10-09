#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:34:28 2019

@author: edoardottt
"""

def estrai_pari_lista2(l):
    '''
    The function take as input a list of integers and returns a new list having
    only the even numbers of the list taking as input. 2nd version
    '''
    lista = []
    for i in range(len(l)):
        if l[i]%2==0:
            lista += [l[i]]
    return lista