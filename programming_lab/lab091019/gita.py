#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:42:11 2019

@author: angelo
"""


def gita(students, ticket):
    if students < 10:
        return students * ticket
    elif students < 30:
        return students * (ticket - ticket * 20 / 100)
    else:
        return students * ticket * 0.7
