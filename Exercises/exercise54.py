#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:47:50 2019

@author: edoardottt
https://edoardoottavianelli.it
"""

# recursion example 2

def recursive_sum(l):
    if len(l)==1: return l[0]
    return l[0] + recursive_sum(l[1:])