#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:15:40 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

#Write a function that take as input a list of integer and returns a list containing the 10-complement 
#of those numbers

def complement_ten(l):
    result = []
    for i in range(len(l)):
        result += [10**len(str(l[i]))-l[i]]
    return result

#without range
def complement_ten2(l):
    result = []
    for i in l:
        result += [10**len(str(i))-i]
    return result
