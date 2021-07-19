#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:26:37 2019

@author: angelo
Write a function that takes as an argument a string containing words separated by spaces and returns a dictionary where the keys are the lengths of the words and values ​​how many words of that length are present in the input string.

ex: "tanti baci a tutti" {1:1, 4:1, 5:2}
"""
from frequency import S


def frequency_lengths(s):
    word = s.split()
    dic = {}
    for word in words:
        if len(word) not in diz:
            dic[len(word)] = 1
        else:
            dic[len(word)] += 1
    return dic


def frequency_lengths2(s):
    word = s.split()
    dic = {}
    for word in words:
        dic[len(word)] = dic.get(len(word), 0) + 1
    return dic
