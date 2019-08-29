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
print(raw_samples.mean(axis=0))
print(raw_samples.std(axis=0))

# sklearn.preprocessing.scale(原始样本矩阵) 
#     --> 均值移除后的样本矩阵
samples = sp.scale(raw_samples)         # 标准化样本均值和标准差(mean=0, std=1)
print('samples:', samples)
print(samples.mean(axis=0))
print(samples.std(axis=0))



std_samples = raw_samples.copy()
for col in std_samples.T:       # h
    col_mean = col.mean()
    col_std = col.std()
    col -= col_mean
    col /= col_std
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
print('\n')
