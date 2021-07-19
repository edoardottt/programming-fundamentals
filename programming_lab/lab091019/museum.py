#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:21:23 2019

@author: angelo
"""


def museum(student, ticket_full):
    """Write a function that gives input the cost of the ticket to visit a museum and the number of students in a class on a school trip, the total cost returns, considering that if the students are between 10 and 30 the ticket per student costs 20 % less, if they are 31 or more 30% less."""
    if student < 10:
        total = student * ticket_full
    elif student <= 30:
        total = (student * ticket_full) * 0.8
    else:
        total = (student * ticket_full) * 0.7
    return total
