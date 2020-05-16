#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:42:25 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

#Write a function that take as input a list of integer and returns the sum of the even numbers minus
#the sum of odd numbers.

l = [1,2,3,4,5,6,7,8,9,10]
# 10 + 8 + 6 + 4 + 2 = 30
# 9 + 7 + 5 + 3 + 1 = 25
# result = 5
def foo(li):
    sum_even = 0
    sum_odd = 0
    for elem in li:
        if elem%2==0:
            sum_even += elem
        else:
            sum_odd += elem
    return sum_even - sum_odd

#with range
def foo2(li):
    sum_even = 0
    sum_odd = 0
    for i in range(len(li)):
        if li[i]%2==0:
            sum_even += li[i]
        else:
            sum_odd += li[i]
    return sum_even - sum_odd
    
#with while

def foo3(li):
    sum_even = 0
    sum_odd = 0
    i = 0
    while i < range(len(li)):
        if li[i]%2==0:
            sum_even += li[i]
        else:
            sum_odd += li[i]
        i+=1
    return sum_even - sum_odd