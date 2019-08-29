# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:26:58 2018

@author: Administrator
"""
'''
机器视觉OpenCV-Python 基本功能   SIFT特征检测器
综合了角点检测 边缘检测等功能
'''
#import numpy as np
import cv2 as cv                   # OpenCV模块
import matplotlib.pyplot as plt

# 读取图片
original = cv.imread('../ML/data/table.jpg')
cv.imshow('Original', original)          # 第一次出现，需要指定窗口名 'Original' + 图片数组original

# 灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# star特征检测
star = cv.xfeatures2d.StarDetector_create()      # star特征检测器
keypoints = star.detect(gray)                    # return: keypoints 关键特征点的集合


# sift特征检测
sift = cv.xfeatures2d.SIFT_create()

'''
特征描述矩阵：star特征检测和sift特征检测的交集
keypoints, desc = shit.compute(gray, star_return): 第二个参数 star特征检测的返回值
'''
keypoints, desc = sift.compute(gray, keypoints)     # 内部调一次sift特征检测方法，然后与star检测进行交集计算，取交集点
print(desc.shape)               # (151, 128)   151个样本，包含128个特征

# 画特征点
mixture = original.copy()
cv.drawKeypoints(original, 
                 keypoints, 
                 mixture,
                 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS    # 绘出详细rich的ketpoint的信息
                 )
cv.imshow('Mixture', mixture)

# desc矩阵图 plt.imshow() / plt.matshow()
plt.matshow(desc,
            cmap='jet',
            fignum='Description')
plt.title('Description')
plt.xlabel('Feature')
plt.ylabel('Sample')
plt.tick_params(which='both', top=False, labeltop=False, labelbottom=False, labelsize=10)

plt.show()