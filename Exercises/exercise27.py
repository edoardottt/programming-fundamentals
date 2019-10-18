#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:51:22 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
'''
Write a function called intreccia that take as input two strings and returns
new one that it's the merge of the two inputs.
Example: intreccia('abc','efg') = 'aebfcg'
'''

def intreccia(s1,s2):
    s1 = s1.replace('',' ').split()
    s2 = s2.replace('',' ').split()
    result = ''
    length = len(s1)+len(s2)
    for i in range(length):
        if i < len(s1):
            result += s1[i]
        if i < len(s2):
            result += s2[i]
    return result

#Version with while
def intreccia2(s1,s2):
    s1 = s1.replace('',' ').split()
    s2 = s2.replace('',' ').split()
    result = ''
    length = len(s1)+len(s2)
    i = 0
    while i < length:
        if i < len(s1):
            result += s1[i]
        if i < len(s2):
            result += s2[i]
        i+=1
    return result