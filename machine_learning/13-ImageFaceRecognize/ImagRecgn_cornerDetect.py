# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:26:58 2018

@author: Administrator
"""
'''
机器视觉OpenCV-Python 基本功能
'''
import numpy as np
import cv2 as cv                   # OpenCV模块

# 读取图片
original = cv.imread('../ML/data/box.png')
cv.imshow('Original', original)          # 第一次出现，需要指定窗口名 'Original' + 图片数组original

# 灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# return: 包含角点信息的图片  哈里斯角点检测
corners = cv.cornerHarris(gray, 7, 5, 0.04)           # 7，5 ： 水平方向阈值，垂直方向阈值；0.04：迭代精度即步长
#cv.imshow('Corners', corners)
print(corners.max())                                    # 0.14142777

# 锐化
corners = cv.dilate(corners, None)                  # 锐化，让边缘更清晰

mixture = original.copy()                           # 视图

# 掩码：
mixture[corners > corners.max() * 0.01] = [0, 0, 255]   # 比0.01*max大的认为是角点, 设为red
cv.imshow('Mixture', mixture)




cv.waitKey(2)