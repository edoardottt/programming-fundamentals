#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:30:48 2019

@author: angelo
"""


def sconto(prezzo, perc_sconto):
    t = prezzo * perc_sconto / 100
    print(prezzo - t)
    return prezzo - t


def sconto2(prezzo, perc_sconto):
    print(prezzo - prezzo / 100 * perc_sconto)
    return prezzo - prezzo / 100 * perc_sconto


def sconto3(prezzo, perc_sconto):
    print(prezzo * (100 - perc_sconto) / 100)
    return prezzo * (100 - perc_sconto) / 100
