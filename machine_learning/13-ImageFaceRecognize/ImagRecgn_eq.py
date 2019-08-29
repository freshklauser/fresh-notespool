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
original = cv.imread('../ML/data/sunrise.jpg')
cv.imshow('Original', original)          # 第一次出现，需要指定窗口名 'Original' + 图片数组original



'''
# 灰度图的均衡直方：
转化为灰度图：不可逆过程
convertcolor (cv.cvtColor(图片变量, cv.COLOR_BGR2GRAY))
均衡直方后的灰度图 (亮度提升,图片不会变模糊)
'''
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
equlized_gray = cv.equalizeHist(gray)           # 均衡直方后的灰度图 (亮度提升,图片不会变模糊)
cv.imshow('Gray', gray)
cv.imshow('Equlized Gray', equlized_gray)



'''
# 彩色图的均衡直方：
1) 获得yuv图
cv.cvtColor(yuv[:,:,0], cv.COLOR_BGR2YUV) :  参数 cv.COLOR_BGR2YUV
yuv：亮度，色度，饱和度 ，不是指RGB
2) 对yuv图的y通道进行均衡直方后convert成BGR :  参数 COLOR_YUV2BGR
cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
    equalizeHist(src[, dst]) -> dst
'''
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
cv.imshow('YUV', yuv)
yuv[:,:,0] = cv.equalizeHist(yuv[:,:,0])
equlized_yuv_rgb = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Equlized_yuv_rgb', equlized_yuv_rgb)




'''
Canny边缘检测
# ,150,240. 为量化精度，水平方向和垂直方向的颜色梯度阈值
# 阈值越小，检测越钝化，很多不是边缘的可能会被认为是边缘
# 阈值越大，检测越灵敏，有可能是边缘的地方会被认为不是边缘
'''
canny = cv.Canny(original, 150, 240)

cv.imshow('Canny', canny)


#cv.waitKey(2)                            # 人为设置阻塞，不设置图片一闪而过，貌似也不会闪过？？？
cv.imwrite('Canny.jpg', canny)
cv.imwrite('Gray.jpg', gray)
cv.imwrite('Equlized Gray.jpg', equlized_gray)


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