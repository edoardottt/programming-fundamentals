# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:55:42 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

#Write a function that take as input two integers and a string.
#Due to the string content, that it will be an operation, the function will execute
#the 4 basic operations with two integers: sum, subtraction, multiplication, division.

def calculate_weird_stuff(string,a,b):
    if (string not in ['+','/','*','-']):
        print('Remember the 4 basic operations are: -,/,*,+')
    else:
        if string=='+':
            tmp = a+b
        elif string=='-':
            tmp = a-b
        elif string =='/':
            tmp = a/b
        elif string =='*':
            tmp = a*b
        print('The result is',tmp)
