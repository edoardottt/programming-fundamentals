#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:24:04 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
'''
Write a function that take as input a list of integers and returns the numbers 
of valleys, keeping in mind that a valley number is a number that 
s[i] < s[i-1] and s[i] < s[i+1].
'''

lista = [1,3,1,5,6,4,7,1,8]

def valley(l):
    valleys = 0
    for i in range(1,len(l)-1):
        if l[i-1] > l[i] < l[i+1]:
            valleys+=1
    return valleys

#Version with while
def valley2(l):
    valleys = 0
    i = 1
    while i < len(l)-1:
        if l[i-1] > l[i] < l[i+1]:
            valleys+=1
        i+=1
    return valleys