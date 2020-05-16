#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:25:48 2019

@author: edoardottt
"""
#Write a function that take as input a string containing some words (sequence of characters separated
#by commas,tabs or new line) and an integer and it returns the number of words in the string having 
#its length equal to the integer taken as input.

def count_words(string,length):
    l = string.split()
    counter = 0
    for i in l:
        if len(i)==length:
            counter+=1
    return counter