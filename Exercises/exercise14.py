# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:38:03 2019

@author: edoardottt
https://www.edoardoottavianelli.it
https://www.github.com/edoardottt
"""

l = [1,2,3,4,5,6,7,8,9] #l list definition
a = l.copy()    #a copy of the list l stored in the variable a
print(a)    
print(id(a)==id(l)) # the function copy returns a different list

l1 = slice(0,3,2)   #slice(start,stop,step)

print(l[l1])    # using slice method to take a sublist
