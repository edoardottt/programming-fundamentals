#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:13:16 2019

@author: angelo
"""


def f():
    r = 1022
    "tough..."
    return r


def g():
    p = 909
    "tougher"
    p += f()
    return p


def h():
    q = 3343
    "very intricate"
    q *= g()
    return q


j = h()
print(j)
