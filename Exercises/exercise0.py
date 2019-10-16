# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:31:58 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

#Write a function that take as input a product's cost and the discount percentage. 
#The function calculates and prints the final cost.

def calculate_cost(price,discount=0):
    if discount>100 or discount<0:
        print("Invalid discount. Remember 0<=discount<=100.")
    else:
        tmp = (price/100)*discount
        price = price - tmp
        print("The final price is",price)
