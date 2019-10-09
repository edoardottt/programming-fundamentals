# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:13:10 2019

@author: edoardott
"""

def invest(capital,interest,years):
    return(int((capital * (1+interest/100)**years)))