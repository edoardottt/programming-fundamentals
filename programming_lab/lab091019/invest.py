#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:13:38 2019

@author: angelo
"""
def invest(capitale, interesse, anni):
    """
Scrivere una funzione 'invest' nel file 'invest.py', che prende in input un capitale, un interesse annuale e un numero di anni e ritorna come intero il capitale maturato dopo un investimento di n anni all'interesse i. Usare la formula maturato = capitale * (1+interesse/100)**anni.
"""
    maturato = capitale * (1+interesse/100)**anni
    return int(maturato)