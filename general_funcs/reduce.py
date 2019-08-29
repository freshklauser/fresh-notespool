# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:31:54 2018

@author: Administrator
"""

import functools

def f1(x, y):
    print(x, y)
    return x + y
    #1 2
    #3 3
    #6 4
    #10 5
    #15 6

a = [1, 2, 3, 4, 5, 6]
b = sum(a)
print(b)        # 21
c = functools.reduce(f1, a)
c1 = functools.reduce(lambda x,y: x + y, a)
print(c, c1)        # 21 21