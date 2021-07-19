#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:13:38 2019

@author: angelo
"""


def invest(capital, interest, years):
    """
    Writing an 'invest' function in the 'invest.py' file, which takes capital as input, an annual interest and a number of years and returns as an integer the capital accrued after an investment of n years to interest i. Use the formula accrued = principal * (1 + interest / 100) ** years."""
    mature = capital * (1 + interest / 100) ** years
    return int(mature)
