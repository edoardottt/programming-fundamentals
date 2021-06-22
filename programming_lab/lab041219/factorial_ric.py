#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:55:46 2019

@author: angelo

Scrivere la funzione factorial ricorsiva.
Ricordarsi che n! = n * (n-1)!

caso_base:     n=1 -> 1
caso_ricorsivo: n>1 -> n * (n-1)!
"""


def factorial_ric(n):
    if n == 1:
        return 1
    return n * factorial_ric(n - 1)
