#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:30:33 2019

@author: angelo
"""


def extract_even(list\):
    """It takes a list of integers and returns a NEW list with only the even elements of the list taken """
    new_list = []
    for element in list:
        if element % 2 == 0:
            new_list.append(element)
    return new_list
