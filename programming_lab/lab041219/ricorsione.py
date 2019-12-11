#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:13:16 2019

@author: angelo
"""

def f():
    r = 1022
    'robatosta...'
    return r

def g():
    p = 909
    'robapiùtosta'
    p += f()
    return p

def h():
    q = 3343
    'robaintricatissima'
    q *= g()
    return q

j = h()
print(j)
