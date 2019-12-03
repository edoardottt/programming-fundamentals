#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:10:43 2019

@author: edoardottt
https://edoardoottavianelli.it
"""
import os

# listing files present in the current directory
def listing_files(path):
    files = os.listdir(path)
    for filename in files:
        print(f"{path}/{filename}")