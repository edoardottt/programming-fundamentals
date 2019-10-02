# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:59:52 2019

@author: edoardottt
"""

import math

#1
#Write a python script that bring as input
#a float number, it calculates the cube root and it prints it in console.

num = float(input())
print(str(num**(1.0/3)))

#2
#Write a python script that bring as input a person name
# and a name of one fruit and it prints: "[name] loves eating [fruit]" 

name = str(input())
fruit = str(input())

print(name+" loves eating "+fruit)

#3
#Write a python script that brings as input two float numbers 'a' and 'b' and it 
#prints 'c'.'c' corresponding to the hypotenuse of the rectangle triangle having
#as catesis two sides a and b,respectively.

cat1 = float(input())
cat2 = float(input())

ipo = ((cat1**2)+(cat2**2))**(0.5)

print(ipo)

#4
#Write a python script that brings as input three float
#numbers a,b,c and it prints the expression: look it on the website

a = float(input())
b = float(input())
c = float(input())

print(a**2+(((b**3)*(c**4))/3*a)-b+a*c)