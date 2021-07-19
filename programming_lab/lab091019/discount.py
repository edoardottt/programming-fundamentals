#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:30:48 2019

@author: angelo
"""


def discount(price, discount_perc):
    t = price * discount_perc / 100
    print(price - t)
    return price - t


def discount2(price, discount_perc):
    print(price - price / 100 * discount_perc)
    return price - price / 100 * discount_perc


def discount3(price, discount_perc):
    print(price * (100 - discount_perc) / 100)
    return price * (100 - discount_perc) / 100
