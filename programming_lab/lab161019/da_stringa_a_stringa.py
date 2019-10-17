#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:20:02 2019

@author: angelo

Scrivere una funzione da_stringa_a_stringa che prende in input una stringa contenente parole separate da spazi e restituisce una nuova stringa con le sole parole di lunghezza l presa come parametro, separate da spazio.

esempio "oggi il sole splende per me", 2 : "il me"
"""

def da_stringa_a_stringa(stringa, l):
    lista = stringa.split()
    lista_parole = []
    for parola in lista:
        if len(parola) == l:
            lista_parole.append(parola)
    return ' '.join(lista_parole)

def da_stringa_a_stringa2(stringa, l):
    lista = stringa.split()
    nuova_stringa = ""
    for parola in lista:
        if len(parola) == l:
            if nuova_stringa == "":
                nuova_stringa = parola
            else:
                nuova_stringa = nuova_stringa + " " + parola
    return nuova_stringa

def da_stringa_a_stringa3(stringa, l):
    lista = stringa.split()
    nuova_stringa = ""
    for parola in lista:
        if len(parola) == l:
                nuova_stringa = nuova_stringa + " " + parola
    return nuova_stringa.lstrip()