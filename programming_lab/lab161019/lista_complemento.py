#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:38:24 2019

@author: angelo

Scrivere una funzione che prende in input una lista di interi e ritorna la lista con i complementi a 10 degli interi della lista in input.
"""

def complemento_a_10(numero):
    n = len(str(numero))
    return 10**n - numero

def lista_complemento(lista_interi):
    lista = []
    for numero in lista_interi:
        lista.append(complemento_a_10(numero))
    return lista

def lista_complemento2(lista_interi):
    lista = []
    for i in range(len(lista_interi)):
        lista.append(complemento_a_10(lista_interi[i]))
    return lista

def lista_complemento3(lista_interi):
    lista = []
    i = 0
    while i < len(lista_interi):
        lista.append(complemento_a_10(lista_interi[i]))
        i+=1
    return lista