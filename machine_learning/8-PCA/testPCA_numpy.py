# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 17:13:04 2018

@author: Administrator
"""

import numpy as np

# 原始样本
A = np.mat('3 2000; 2 3000; 4 5000; 5 8000; 1 2000', dtype=float)
print('A:', A, sep='\n')
print(A.shape)

# 均值为0, 极差为1
mu = A.mean(axis=0)
print(mu.shape, type(mu))
# print(mu)
s = A.max(axis=0) - A.min(axis=0)       # axis=0
X = (A - mu) / s
print('X:', X, type(s), sep='\n')
# X各维特征的协方差矩阵
# SIGMA = X.T * X        # 与下一行代码的最后结果一样，中间SIGMA和S不一样，U和V一样
SIGMA = np.mat(np.cov(X, rowvar=0))
print('SIGMA:----', SIGMA, sep='\n')
# 奇异值分解
U, S, V = np.linalg.svd(SIGMA)
print(type(U), '---')
print('U:', U, sep='\n')
print('S:', S, sep='\n')
# [1.2589664  0.08825582]  1.26大，选择第一个特征U[:,0]作为主成分特征
print('V:', V, sep='\n')
# 主成分特征矩阵 U靠前的是主成分矩阵
U_reduce = U[:, 0]
print('U_reduce:', U_reduce, sep='\n')
# 降维样本
Z = X * U_reduce
print('Z:', Z, sep='\n')

# 恢复到均值极差转换之前
X_approx = Z * U_reduce.T
print('X_approx:', X_approx, sep='\n')
# 恢复到原始样本
A_approx = np.multiply(X_approx, s) + mu    # 对应元素相乘
print('A_approx:', A_approx, A, sep='\n')
