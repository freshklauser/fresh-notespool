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
original = cv.imread('forest.jpg')
print(original.shape)                   # (397, 600, 3)-(水平像素, 垂直像素, BGR3种通道)
cv.imshow('Original', original)         # 第一次出现，需要指定窗口名 'Original' + 图片数组original

blue = np.zeros_like(original)
blue[...,0] = original[...,0]           # 0 - 蓝色通道
cv.imshow('Blue', blue)

green = np.zeros_like(original)
green[...,1] = original[...,1]          # 1 - 红色通道
cv.imshow('Green', green)

red = np.zeros_like(original)
red[...,2] = original[...,2]            # 2 - 绿色通道
cv.imshow('Red', red)



# 截取图片, 数组切片
h, w = original.shape[:2]                   # 高，宽 (单位：像素)
print(h,w)
l, t = int(w *3 / 4), int(h *3 / 4)         # 左上角  左，顶
r, b = int(w), int(h)     # 右下角  右，底
cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)



# 变形，缩放：颜色采用插值进行中间色平均
'''
scaled = cv.resize(original, (w * 2, int(h / 2)), interpolation=cv.INTER_LINEAR)
'''
# 宽度扩大2倍后，新增的像素点颜色用插值法进行填充
scaled = cv.resize(original, None, fx=2, fy=0.5, interpolation=cv.INTER_LINEAR)
# fx=2: 水平方向放大2倍； fy=0.5:垂直方向缩小0.5倍
cv.imshow('Scaled', scaled)


cv.waitKey(2)                            # 人为设置阻塞，不设置图片一闪而过



# 保存
cv.imwrite('blue.jpg', blue)
cv.imwrite('red.jpg', red)
cv.imwrite('green.jpg', green)


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