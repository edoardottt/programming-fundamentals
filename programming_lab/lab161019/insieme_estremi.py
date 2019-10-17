#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:28:14 2019

@author: angelo

Scrivere una funzione che prende come argomento una lista di interi e due interi e ritorna l'insieme degli elementi compresi fra i due interi presi come parametro che sono presenti nella lista.

esempio [56, 12, 8, 100] 5,15 {8,12}
"""
def insieme_estremi(lista, a, b):
    s = set()
    for el in lista:
        if a <= el <=b:
            s.add(el)
    return s

def insieme_estremi2(lista, a, b):
    s = set(lista)
    estremi = set(range(a,b+1))
    return s & estremi



def conta(lista, estremoa, estremob):
    s = set()
    for el in lista:
        if estremoa < el < estremob:
            s.add(el)
    return s


def conta2(lista, estremoa, estremob):
    s = set()
    insieme = set(lista)
    for el in range(estremoa, estremob+1):
        if el in insieme:
            s.add(el)
    return s

def conta3(lista, estremoa, estremob):
    insieme = set(lista)
    estremi = set(range(estremoa, estremob+1))
    return insieme.intersection(estremi)

def conta4(lista, estremoa, estremob):
    s = set()
    insieme = set(lista)
    i = estremoa
    while i < estremob:
        if i in insieme:
            s.add(i)
        i+=1
    return s

def conta5(lista, estremoa, estremob):
    s = set()
    i = estremoa
    while i < estremob:
        if i in lista:
            s.add(i)
        i+=1
    return s
