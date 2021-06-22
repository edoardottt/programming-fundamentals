#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:42:11 2019

@author: angelo
"""


def gita(studenti, biglietto):
    if studenti < 10:
        return studenti * biglietto
    elif studenti < 30:
        return studenti * (biglietto - biglietto * 20 / 100)
    else:
        return studenti * biglietto * 0.7
