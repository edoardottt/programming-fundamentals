#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:57:29 2019

@author: angelo
Scrivere una funzione che prende in input una lista di interi e ritorna la lista con i complementi a 10 degli interi della lista in input
"""


def calcola_complemento(numero):
    n = len(str(numero))
    complemento = 10 ** n - numero
    return complemento


def calcola_complemento2(numero):
    n = 1
    a = numero
    while a // 10 > 0:
        n += 1
        a //= 10
    complemento = 10 ** n - numero
    return complemento


def lista_complementi(lista):
    complementi = []
    for numero in lista:
        complemento = calcola_complemento(numero)
        complementi.append(complemento)
    return complementi


def lista_complementi2(lista):
    complementi = []
    for i in range(len(lista)):
        complemento = calcola_complemento(lista[i])
        complementi.append(complemento)
    return complementi


def lista_complementi3(lista):
    complementi = []
    i = 0
    while i < len(lista):
        complemento = calcola_complemento(lista[i])
        complementi.append(complemento)
        i = i + 1
    return complementi


def lista_complementi4(lista):
    complementi = []
    for numero in lista:
        complemento = calcola_complemento2(numero)
        complementi.append(complemento)
    return complementi
