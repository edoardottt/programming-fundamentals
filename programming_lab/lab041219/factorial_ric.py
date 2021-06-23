#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:55:46 2019

@author: angelo

Write the recursive factorial function.
Remember that n! = n * (n-1)!

base_case:     n=1 -> 1
recursive_case: n>1 -> n * (n-1)!
"""


def factorial_ric(n):
    if n == 1:
        return 1
    return n * factorial_ric(n - 1)
