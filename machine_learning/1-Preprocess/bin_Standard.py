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
1）均值移除：为了统一样本矩阵中不同特恒的基准值和分散度，可以将各个特征的
         平均值调整为0，标准差调整为1，这个过程称为均值移除。
sklearn.preprocessing.scale(原始样本矩阵) 
    --> return：均值移除后的样本矩阵(mean=0, std=1)
def scale(X, axis=0, with_mean=True, with_std=True, copy=True):
    Standardize a dataset along any axis
'''
samples = sp.scale(raw_samples) # 标准化样本均值和标准差(mean=0, std=1)
print('samples:', samples)
print(samples.mean(axis=0))     # [ 5.55111512e-17 -1.11022302e-16 -7.40148683e-17 -7.40148683e-17]
print(samples.std(axis=0))      # [1. 1. 1. 1.]


'''
2）范围缩放：统一样本矩阵中不同特征的最大值和最小值范围
sklearn.preprocessing.MinMaxScaler(feature_range=期望最小最大值, copy=True)
    --> return: 范围缩放器
                范围缩放器.fit_transform(原始样本矩阵)
                    --> return：范围缩放后的样本矩阵
    Parameters
    ----------
    feature_range : tuple (min, max), default=(0, 1)
        Desired range of transformed data.
    copy : boolean, optional, default True
        Set to False to perform inplace row normalization and avoid a
        copy (if the input is already a numpy array).
'''
mms = sp.MinMaxScaler(feature_range=(0, 1))         # 样本标准化到(0,1)之间
mms_samples = mms.fit_transform(raw_samples)        # 缩放后的样本矩阵
print(mms_samples)                                  # range(0,1)
#[[1.         0.         1.         0.        ]
# [0.         1.         0.41025641 1.        ]
# [0.33333333 0.87272727 0.         0.14666667]]


'''
3）归一化：为了用占比表示特征，用每个样本的特征值除以该样本的特征值绝对值之和，以
        使每个样本的特征值绝对值之和为1。 （转化为占比 normalized）
sklearn.preprocessing.normalize(原始样本矩阵，norm='l1')
	--> return：归一化后的样本矩阵
l1即L1范数，矢量中各元素绝对值之和。
l2即L2范数，矢量元素绝对值的平方和再开方
def normalize(X, norm='l2', axis=1, copy=True, return_norm=False):
    norm : 'l1', 'l2', or 'max', optional ('l2' by default)
    The norm to use to normalize each non zero sample (or each non-zero feature if axis is 0).
'''
nor_samples = sp.normalize(raw_samples, norm='l1')  # 归一化：百分比
print(nor_samples)


'''
4）二值化：用0和1来表示样本矩阵中相对于某个给定阈值高于或低于它的元素
sklearn.preprocessing.Binarizer(threshold=阈值, copy=True)        # copy default True
    --> return：二值化器
                二值化器.transform(原始样本矩阵) 
                    --> return: 二值化后的样本矩阵 （不可逆过程）--考虑独热编码
threshold: feature <= threshold: feature = 0;
                    > threshold: feature = 1.
'''
bins = sp.Binarizer(threshold=1.4)              # 构建二值化器
bins_samples = bins.transform(raw_samples)      # 样本二值转换， 不可逆
print(bins_samples)


'''
5）独热编码
'''
sp.Binarizer()












