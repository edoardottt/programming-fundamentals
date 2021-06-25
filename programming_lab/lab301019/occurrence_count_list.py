#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:25:33 2019

@author: angelo
Writing a function that takes a list returns a new list made up of tuples. 
Each tuple has the first element which is an element of the input list and has the second element equal to the number of times the first element is repeated in the list.

ex:
    [1,2,2,2,"b","a","a",2.0,2.0,2.0,"casa",2.0,"home"]
    return a list [(1,1), (2,3), ("b",1), ("a",2), (2.0,4), ("home",2)]

"""


def occurance_count_list(list):
    dic = {}
    for element in list:
        count = 0
        if element not in dic:
            for i in list:
                if element == i:
                    count += 1
            dic[element] = count
    return list(dic.items())


def occurance_count_list2(list):
    dic = {}
    for element in list:
        if element not in dic:
            dic[element] = list.count(element)
    return list(dic.items())


def occurance_count_list3(list):
    dic = {}
    for element in list:
        tuple = element, type(element)
        if tuple not in dic:
            dic[tuple] = 1
        else:
            dic[tuple] += 1
    return [(tuple[0], dic[tuple]) for tuple in dic]


def occurance_count_list4(list):
    dic = {(x, type(x)): 0 for x in list}
    for element in list:
        dic[(element, type(element))] += 1
    return [(el[0], dic[el]) for el in dic]
