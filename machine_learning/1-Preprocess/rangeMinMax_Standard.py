# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 11:22:34 2018

@author: Administrator
"""

import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
        [3, -1.5, 2, -5.4],
        [0, 4, -0.3, 2.1],
        [1, 3.3, -1.9, -4.3]])
print(raw_samples)

'''
sklearn.preprocessing.scale(原始样本矩阵) 
    --> 均值移除后的样本矩阵
'''
samples = sp.scale(raw_samples)         # 标准化样本均值和标准差(mean=0, std=1)
print('samples:', samples)
print(samples.mean(axis=0))
print(samples.std(axis=0))

'''
sklearn.preprocessing.MinMaxScaler(feature_range=期望最小最大值)
	--> return: 范围缩放器
范围缩放器.fit_transform(原始样本矩阵)
	--> return：范围缩放后的样本矩阵
'''
mms = sp.MinMaxScaler(feature_range=(0, 1))         # 样本标准化到(0,1)之间
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)











# ********************************************
# Test 原始方法
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([[col_min, 1],
                  [col_max, 1]])
    b = np.array([0, 1])            # [min, max]
    x = np.linalg.lstsq(a, b, rcond=1)[0]           # 需要再复习一下返回值
    col *= x[0]
    col +=x[1]
print(mms_samples)