#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:17:48 2019

@author: edoardottt
https://edoardoottavianelli.it
"""

#Listing all files in the 'path' directory and in all the subdir of path
import os

def recursive_listing_files(path):
    dirs = os.listdir(path)
    if len(dirs)==0: pass
    else:
        for filename in dirs:
            fullpath = f"{path}/{filename}"
            if os.path.isdir(fullpath): recursive_listing_files(fullpath)
            else: print(fullpath)
            
recursive_listing_files('/home/edoardottt/GITHUB')