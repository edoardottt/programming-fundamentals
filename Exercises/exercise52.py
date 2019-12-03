#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:58:42 2019

@author: edoardottt
https://edoardoottavianelli.it
"""

# Count recursively the files into the input directory
import os

def dimensioni_dir(path):
    dim = 0
    for name in os.listdir(path):
        fullname = path + "/" + name
        if os.path.isdir(fullname):
            dim += dimensioni_dir(fullname)
        else:
            dim += 1
    return dim