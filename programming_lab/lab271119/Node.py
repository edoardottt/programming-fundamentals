#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:13:25 2019

@author: angelo
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.leftchild = None
        self.rightchild = None

    def add_node(self, val):
        if self.val > val:
            if not self.leftchild:
                self.leftchild = Node(val)
            else:
                self.leftchild.add_node(val)
        else:
            if not self.rightchild:
                self.rightchild = Node(val)
            else:
                self.rightchild.add_node(val)

    def printing(self, l=[]):
        l.append(self.val)
        if self.leftchild:
            print("Left recursion nodes", l)
            self.leftchild.printing(l)
        print(self.val, end=" ")
        if self.rightchild:
            print("Right recursion nodes", l)
            self.rightchild.printing(l)
        l.pop()

    def create_tree_from_list(l):
        root = Node(l[0])
        for i in l[1:]:
            root.add_node(i)
        return root

    def find(self, val):
        if self.val == val:
            return True
        if val < self.val:
            next = self.leftchild
        else:
            next = self.rightchild
        if next:
            return next.find(val)
        return False
