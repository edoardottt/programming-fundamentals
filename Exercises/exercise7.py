#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:25:37 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

def estrai_pari_lista(l):
    '''
    The function take as input a list of integers and returns a new list having
    only the even numbers of the list taking as input.
    '''
    lista = []
    for elem in l:
        if elem%2==0:
            lista.append(elem)
    return lista
