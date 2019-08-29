# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:26:58 2018

@author: Administrator
"""
'''
机器视觉OpenCV-Python 基本功能   star特征检测
综合了角点检测 边缘检测等功能
'''
import numpy as np
import cv2 as cv                   # OpenCV模块

# 读取图片
original = cv.imread('../ML/data/table.jpg')
cv.imshow('Original', original)          # 第一次出现，需要指定窗口名 'Original' + 图片数组original

# 灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# star特征
star = cv.xfeatures2d.StarDetector_create()      # star特征检测器
keypoints = star.detect(gray)                    # keypoints：关键特征点的集合
print(type(star))                               # <class 'cv2.xfeatures2d_StarDetector'>

mixture = original.copy()
cv.drawKeypoints(original, 
                 keypoints, 
                 mixture,
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS    # 绘出详细rich的ketpoint的信息
                 )
cv.imshow('Mixture', mixture)



cv.waitKey()                # 按ESC键 结束程序，也可以自己设置delay