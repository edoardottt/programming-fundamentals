#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:25:33 2019

@author: angelo
Scrivere una funzione che presa una lista restituisce una nuova lista composta da tuple. Ogni tupla ha il primo elemento che è un elemento della lista in ingresso e ha il secondo elemento pari al numero di volte che il primo elemento si ripete nell lista.

es:
    [1,2,2,2,"b","a","a",2.0,2.0,2.0,"casa",2.0,"casa"]
    ritorna la lista [(1,1), (2,3), ("b",1), ("a",2), (2.0,4), ("casa",2)]

"""


def conta_occorrenze_lista(lista):
    diz = {}
    for elemento in lista:
        conta = 0
        if elemento not in diz:
            for i in lista:
                if elemento == i:
                    conta += 1
            diz[elemento] = conta
    return list(diz.items())


def conta_occorrenze_lista2(lista):
    diz = {}
    for elemento in lista:
        if elemento not in diz:
            diz[elemento] = lista.count(elemento)
    return list(diz.items())


def conta_occorrenze_lista3(lista):
    diz = {}
    for elemento in lista:
        tupla = elemento, type(elemento)
        if tupla not in diz:
            diz[tupla] = 1
        else:
            diz[tupla] += 1
    return [(tupla[0], diz[tupla]) for tupla in diz]


def conta_occorrenze_lista4(lista):
    diz = {(x, type(x)): 0 for x in lista}
    for elemento in lista:
        diz[(elemento, type(elemento))] += 1
    return [(el[0], diz[el]) for el in diz]
