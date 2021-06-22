#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:50:21 2019

@author: edoardottt
https://edoardoottavianelli.it
"""

# Listing all .txt files in the input directory
import os


def list_txt_files(path):
    dirs = os.listdir(path)
    if len(dirs) == 0:
        pass
    else:
        for filename in dirs:
            fullpath = f"{path}/{filename}"
            if os.path.isdir(fullpath):
                list_txt_files(fullpath)
            elif filename[-4:] == ".txt":
                print(fullpath)
