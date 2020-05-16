#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:26:29 2019

@author: edoardottt
"""

#Write a function that take as input three numbers g,m,a (with a odd, in this way we avoid leap years)
# and it returns True or False depending on the three numbers make a valid date.
#Es. 30/2/2017 False; 1/1/1111 True

def verify_date(g,m,a):
    if a > 2019 or (a==2019 and m> 10) or (a==2019 and m==10 and g>16):
        return False
    elif g>30 and (m==4 or m==6 or m==9 or m==11):
        return False
    elif g>28 and m==2:
        return False
    return True