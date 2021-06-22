# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:48:24 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

# Write a function that take as input a list. the function have to delete the
# integer from the list and returns the number of elements deleted.


def delete_integer(l):
    counter = 0
    for i in range(len(l)):
        for item in l:
            if type(item) == int:
                l.remove(item)
                counter += 1
    return counter


l = [1.1, 2, 3, 4, 5, 6, 7, 8, 9]
print(delete_integer(l))
print(l)
