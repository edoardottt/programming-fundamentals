#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:04:19 2019

@author: edoardottt
https://edoardoottavianelli.it
"""
"""
Write a recursive function that take as input a string and returns True
if the input string is palindrome, False altrimenti.
"""


def is_pal(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_pal(s[1:-1])
