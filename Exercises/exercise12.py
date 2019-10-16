#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:56:28 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""


'''
This function returns the strings in a list but with all strings with uppercase.
2nd version
'''
l = ['aNaNas','cocco','Banana','SUSINA']
def print_list_uppercase(l):
    for i in range(len(l)):
        print(l[i].upper())
print_list_uppercase(l)
