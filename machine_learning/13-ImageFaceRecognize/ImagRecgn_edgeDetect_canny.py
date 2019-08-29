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

#original = cv.imread('../ML/data/chair.jpg')
original = cv.imread('baby.jpg')
cv.imshow('Original', original)          # 第一次出现，需要指定窗口名 'Original' + 图片数组original

'''
Canny边缘检测
# ,150,240. 为量化精度，水平方向和垂直方向的颜色梯度阈值
# 阈值越小，检测越钝化，很多不是边缘的可能会被认为是边缘
# 阈值越大，检测越灵敏，有可能是边缘的地方会被认为不是边缘
'''
canny = cv.Canny(original, 150, 250)

cv.imshow('Canny', canny)

#cv.waitKey(2)                            # 人为设置阻塞，不设置图片一闪而过，貌似也不会闪过？？？


'''
cv2坐标系
----------------------
0-------------------->x
|
|
|
|
|
v
y



'''