#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:16:46 2019

@author: edoardottt
https://edoardoottavianelli.it
"""
# recursion example

def find_max(l):
    if len(l)==1:
        return l[0]
    remain = find_max(l[1:])
    if l[0] > remain:
        return l[0]
    return remain