#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:07:10 2019

@author: angelo
"""


def opera(a, b, operazione):
    """
    Scrivere una funzione che prende in input due interi e una stringa. In base al contenuto della stringa, che conterrà una operazione, la funzione eseguirà le 4 operazioni di base con i due interi: addizione, sottrazione, moltiplicazione, divisione.
    """
    if operazione == "+" or operazione.lower() == "addizione":
        return a + b
    elif operazione == "-" or operazione.lower() == "sottrazione":
        return a - b
    elif operazione == "*" or operazione.lower() == "moltiplicazione":
        return a * b
    elif operazione == "/" or operazione.lower() == "divisione":
        return a / b
    else:
        return 0
