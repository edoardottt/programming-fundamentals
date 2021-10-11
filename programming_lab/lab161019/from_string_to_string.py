#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:20:02 2019

@author: angelo

Write a from_string_to_string function that takes as input a string containing words separated by spaces and returns a new string with only words of length l taken as a parameter, separated by spaces.

example "today the sun is shining for me", 2: "the me"
"""


def from_string_to_string(string, l):
    list = string.split()
    list_word = []
    for word in list:
        if len(word) == l:
            list_word.append(word)
    return " ".join(list_word)


def from_string_to_string2(string, l):
    list = string.split()
    new_string = ""
    for word in list:
        if len(word) == l:
            if new_string == "":
                new_string = word
            else:
                new_string = new_string + " " + word
    return new_string


def from_string_to_string3(string, l):
    list = string.split()
    new_string = ""
    for word in list:
        if len(word) == l:
            new_string = new_string + " " + word
    return new_string.lstrip()
