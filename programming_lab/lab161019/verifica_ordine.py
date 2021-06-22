#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:12:23 2019

@author: angelo
Scrivere una funzione che verifica se una lista è ordinata in modo crescente (<=) (supponiamo che la lista contenga oggetti ordinabili).

"""


def verifica_ordine(lista):
    for i in range(len(lista) - 1):
        if lista[i] <= lista[i + 1]:
            continue
        else:
            return False
    return True


def verifica_ordine2(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def verifica_ordine3(lista):
    a = lista[0]
    for elemento in lista[1:]:
        if a > elemento:
            return False
        a = elemento
    return True


def verifica_ordine4(lista):
    i = 0
    while i < len(lista) - 1 and lista[i] <= lista[i + 1]:
        i += 1
    #    if i < len(lista) -1:
    #        return False
    #    return True
    return False if i < (len(lista) - 1) else True


def verifica_ordine5(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            return False
        i = i + 1
    return True
