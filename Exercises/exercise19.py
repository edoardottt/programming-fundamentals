#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:46:08 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

# Write a function that take as input a string with words separated by spaces and returns a list
# containing the length of words

s = "hi my name is edoardottt"


def count_words(s):
    l = s.split()
    result = []
    for i in l:
        result += [len(i)]
    return result


print(count_words(s))
