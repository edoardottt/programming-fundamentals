# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:40:55 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

#Write a function that take as input the ticket price for visiting a museum and the number
#of students of a classroom on school trip. The function has to return the total price,
#taking in mind that if the students number are between 10 and 30, the ticket costs 20% less,
# if they are 31 or more, the ticket will cost 30% less.

def ticket_total_price(price,tickets=1):
    if (tickets>=10 and tickets<=30):
        discount = 20
    elif tickets>30:
        discount = 30
    else:
        discount = 0
    discounted = price-(price/100)*discount
    print(discounted*tickets)
