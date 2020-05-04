# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 11:37:20 2018

@author: Administrator
"""

import sklearn.datasets as sd
import sklearn.decomposition as dc
import matplotlib.pyplot as plt
import numpy as np

x, y = sd.make_circles(n_samples=500,
                       factor=0.2,                  # Scale factor between inner and outer circle.
                       noise=0.04                   # 噪声
                       )
print(x.shape, y.shape)                             # (500, 2) (500,)
print(set(y), '==', np.unique(y))                   # {0, 1} == [0 1], label去重，后者自动排序

# KPCA模型
model = dc.KernelPCA(kernel='rbf',                  # 核函数，与SVM的kernel一样
                     gamma=10,
                     fit_inverse_transform=True)    # fit_inverse_transform=True  ???????????
# 保证model.fit_transform(x)执行升维后会执行PCA降维
kpca_x = model.fit_transform(x)                     # 先核函数升维，再PCA降维
print(kpca_x.shape)                                 # (500, 467) --> (500, 453) 只有前两列有用.其他特征不需要

plt.figure('Original')
plt.subplot(121)
plt.title('Original')
plt.xlabel('x')
plt.ylabel('y')
plt.tick_params(labelsize=10)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y, cmap='brg', alpha=0.5)              # 线性不可分
# plt.scatter(kpca_x[:, 0], kpca_x[:, 1], s=50, c=y, cmap='brg', alpha=0.5)     # 线性可分

plt.subplot(122)
plt.title('kpca')
plt.xlabel('x')
plt.ylabel('y')
plt.tick_params(labelsize=10)
# plt.scatter(x[:, 0], x[:, 1], s=50, c=y, cmap='brg', alpha=0.5)              # 线性不可分
plt.scatter(kpca_x[:, 0], kpca_x[:, 1], s=50, c=y, cmap='brg', alpha=0.5)     # 线性可分
plt.show()
