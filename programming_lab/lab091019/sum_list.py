#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:14:55 2019

@author: angelo
"""


def sum_list(list):
    sum = 0
    for element in list:
        if type(element) == int:
            sum += element
    return sum
