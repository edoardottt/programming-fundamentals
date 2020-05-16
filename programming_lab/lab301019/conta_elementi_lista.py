#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:52:14 2019

@author: angelo
Scrivere una funzione che prende una lista e restituisce una nuova lista composta da tuple. Ogni elemento della tupla ha il primo elemento che è un elemento della lista in input e il secondo che è il numero di volte che l'elemento si ripete a partire da quella posizione. Gli stessi elementi devono essere nello stesso ordine della lista in input.

es: [1,2,2,2,"b","a","a",2.0,2.0,2.0,"casa","casa",2.0]
restituisce
[(1,1),(2,3),("b",1),("a",2),(2.0,4),("casa",2)]
"""

def conta_elementi_lista(lista):
    diz = {}
    for elemento in lista:
        diz[elemento] = lista.count(elemento)
    return list(diz.items())

def conta_elementi_lista2(lista):
    diz = {}
    for elemento in lista:
        if elemento not in diz:
            diz[elemento] = lista.count(elemento)
    return list(diz.items())

def conta_elementi_lista3(lista):
    diz = {}
    for elemento in lista:
        if elemento not in diz:
            diz[elemento] = 1
        else:
            diz[elemento] += 1
    return list(diz.items())


def conta_elementi_lista4(lista):
    diz = {}
    for elemento in lista:
        t = elemento, type(elemento)
        if t not in diz:
            diz[t] = 1
        else:
            diz[t] += 1
    lista_ret = []
    for tupla, ripetizioni in diz.items():
        lista_ret.append((tupla[0], ripetizioni))
    return lista_ret


def conta_elementi_lista5(lista):
    diz = {(elemento, type(elemento)):0 for elemento in lista}
    for elemento in lista:
        t = elemento, type(elemento)
        diz[t] += 1
    return [(tupla[0],diz[tupla]) for tupla in diz]


def conta_elementi_lista6(lista):
    diz = {}
    for elemento in lista:
        try:
            diz[elemento] += 1
        except:
            diz[elemento] = 1
    return list(diz.items())

def conta_elementi_lista7(lista):
    diz = {}
    for elemento in lista:
        diz[elemento] = diz.get(elemento, 0) + 1
    return list(diz.items())

