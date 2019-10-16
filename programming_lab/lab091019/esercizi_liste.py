#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:25:16 2019

@author: angelo
"""

""" Scrivere una funzione che prende una lista di interi e restituisce una nuova lista con i soli elementi pari della lista originaria """

def elementi_pari(lista):
    lista_pari = []
    for i in lista:
        if i % 2 == 0:
            lista_pari.append(i)
    return lista_pari


def elementi_pari_indici(lista):
    lista_pari =[]
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pari.append(lista[i])
    return lista_pari

""" Scrivere una funzione che prende una lista di interi e restituisce un intero corrispondente alla somma di tutti i valori della lista originaria """

def somma_lista(lista):
    somma= 0
    for i in lista:
        somma += i
    return somma


""" Scrivere una funzione che prende una lista di stringhe e restituisce una lista con le sole stringhe che sono una vocale """

def cerca_vocali(lista):

def cerca_vocali_indici(lista):