#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:07:10 2019

@author: angelo
"""


def opera(a, b, operation):
    """
    Write a function that takes two integers and a string as input. Based on the content of the string, which will contain an operation, the function will perform the 4 basic operations with the two integers: addition, subtraction, multiplication, division.
    """
    if operation == "+" or operation.lower() == "addition":
        return a + b
    elif operation == "-" or operation.lower() == "subtraction":
        return a - b
    elif operation == "*" or operation.lower() == "multiplication":
        return a * b
    elif operation == "/" or operation.lower() == "division":
        return a / b
    else:
        return 0
