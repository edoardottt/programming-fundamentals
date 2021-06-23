#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:31:34 2019

@author: angelo
Write a recursive sum_list_even function
returns the sum of all even numbers in the list

sum_even([1,2,3,4]) = if(1=even:1 else 0) + sum([2,3,4]) = ... if(2=even:2 else 0) + sum([3,4])
sum([]) = 0
=
CODICE DESCRIPTION 57S6HE9N
"""


def sum_list_even(l):
    if l == []:
        return 0
    partial_sum = sum_list_even(l[1:])
    # Module 2 returns 1 (i.e. True) if diseven
    if l[0] % 2:
        return partial_sum
    return l[0] + partial_sum
