# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:24:41 2018

@author: Administrator
"""

def f1(x):
    return x + 3

x = 1
y = f1(1)

X = [1 ,2, 3]
Y = list(map(f1, X))        # 矢量运算
Y1 = list(map(lambda x:x+3, X))
print(y, Y, Y1, sep='\n')
#4
#[4, 5, 6]
#[4, 5, 6]