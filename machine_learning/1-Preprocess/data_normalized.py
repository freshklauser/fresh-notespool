# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:54:34 2018

@author: Administrator
"""


import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([
        [3, -1.5, 2, -5.4],
        [0, 4, -0.3, 2.1],
        [1, 3.3, -1.9, -4.3]])

'''
均值移除：为了统一样本矩阵中不同特恒的基准值和分散度，可以将各个特征的
         平均值调整为0，标准差调整为1，这个过程称为均值移除。
sklearn.preprocessing.scale(原始样本矩阵) 
    --> return：均值移除后的样本矩阵
'''
samples = sp.scale(raw_samples)         # 标准化样本均值和标准差(mean=0, std=1)
print('samples:', samples)
print(samples.mean(axis=0))
print(samples.std(axis=0))


'''
范围缩放：统一样本矩阵中不同特征的最大值和最小值范围
sklearn.preprocessing.MinMaxScaler(feature_range=期望最小最大值)
    --> return: 范围缩放器
范围缩放器.fit_transform(原始样本矩阵)
    --> return：范围缩放后的样本矩阵
'''
mms = sp.MinMaxScaler(feature_range=(0, 1))         # 样本标准化到(0,1)之间
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)

'''
归一化：为了用占比表示特征，用每个样本的特征值除以该样本的特征值绝对值之和，以
        使每个样本的特征值绝对值之和为1。 （转化为占比 normalized）
sklearn.preprocessing.normalize(原始样本矩阵，norm='l1')
	--> return：归一化后的样本矩阵
l1即L1范数，矢量中各元素绝对值之和。
'''
nor_samples = sp.normalize(raw_samples, norm='l1')
print(nor_samples)


'''
二值化：用0和1来表示样本矩阵中相对于某个给定阈值高于或低于它的元素
'''















