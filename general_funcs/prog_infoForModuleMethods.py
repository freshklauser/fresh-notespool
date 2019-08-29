# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:33:51 2018

@author: Administrator
"""
# points-1:
# 0和1相当于一个开关，为0时打开b开关，为1时打开a开关
#0 and 'a' or 'b'        # 逻辑运算原则，见个人博客
# 'b'
#1 and 'a' or 'b'
# 'a'

# points-2:
#lambda s: ''

# points-3:
# str的方法：  .join, .split,  ljust(左对齐并用指定字符填充空位)

#--------------------------------分割线--------------------------------------
# 查询方法，并打印出详细说明
import requests
import pandas
import numpy
import os
import lxml
from bs4 import BeautifulSoup
import math
import random
from multiprocessing import Manager,Pool
import collections


# 构造processFun函数并返回
#def printInfo(s, collapse=0):
#    processFun = collapse and (lambda s:' '.join(s.split())) or (lambda s:s)
#    return processFun(s)

def info(object, spacing=15, collapse=0):
    '''
    遍历一遍Object对象，把里面可以被调用的doc string打印出来
    '''
    # 第一步：提取出当前Object可以被调用的方法列表
    methodList = [method for method in dir(object) if callable(
            getattr(object, method))]
    
    # 第二步：需要把doc string的方法按照一个格式提取出来. 构造函数processFun
    processFun = collapse and (lambda s:' '.join(s.split())) or (lambda s:s)
    
    # 第三步： 打印出方法的名称及其文档的说明
    print('\n\n'.join(['%s %s'%( method.ljust(spacing), processFun(
            str(getattr(object, method).__doc__)) ) for method in methodList]))
    # processFun的传参必须是str, getattr()不一定全是str
    
# 执行
info(collections,collapse=1)
print('----------------------------')
print(dir(collections))
















    