#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:58:11 2019

@author: edoardottt
https://edoardoottavianelli.it
"""

# recursive factorial 

def recursive_factorial(n):
    if n==1: return 1
    return n * recursive_factorial(n-1)