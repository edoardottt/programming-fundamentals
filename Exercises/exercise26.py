#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:22:18 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""
'''
Write a function that take as input two strings that represent a sequence of 
integers separated by commas and returns a string in the same format of the 
input strings contaning only the elements of the first string having the 
square rootin th second list, sorted.
'''

stringa1 = '1,3,4,5,6,7,8,9,2'
stringa2 = '4,16,36,64'

def foo(s1,s2):
    s1 = s1.split(',')
    s2 = s2.split(',')
    result = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if int(s1[i])**2==int(s2[j]):
                result += [int(s1[i])]
    result.sort()
    res = ''
    for item in result:
        res+=str(item)+','
    return res[:-1]

#Version without range
def foo2(s1,s2):
    s1 = s1.split(',')
    s2 = s2.split(',')
    result = []
    for i in s1:
        for j in s2:
            if int(i)**2==int(j):
                result += [i]
    result.sort()
    res = ''
    for item in result:
        res+=str(item)+','
    return res[:-1]

#Version with while
def foo3(s1,s2):
    s1 = s1.split(',')
    s2 = s2.split(',')
    result = []
    i,j = 0,0
    while i < len(s1):
        j = 0
        while j < len(s2):
            if int(s1[i])**2==int(s2[j]):
                result += [s1[i]]
            j +=1
        i +=1
    result.sort()
    res = ''
    for item in result:
        res+=str(item)+','
    return res[:-1]