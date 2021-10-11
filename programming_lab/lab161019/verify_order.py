#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:12:23 2019

@author: angelo
Write a function that checks if a list is sorted in ascending order (<=) (suppose the list contains sortable objects).

"""


def verify_order(list):
    for i in range(len(list) - 1):
        if list[i] <= list[i + 1]:
            continue
        else:
            return False
    return True


def verify_order2(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True


def verify_order3(list):
    a = list[0]
    for element in list[1:]:
        if a > element:
            return False
        a = element
    return True


def verify_order4(list):
    i = 0
    while i < len(list) - 1 and list[i] <= list[i + 1]:
        i += 1
    #    if i < len(list) -1:
    #        return False
    #    return True
    return False if i < (len(list) - 1) else True


def verify_order5(list):
    i = 0
    while i < len(list) - 1:
        if list[i] > list[i + 1]:
            return False
        i = i + 1
    return True
