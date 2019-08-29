# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:12:18 2018

@author: Administrator
"""
'''
sklearn.linear_model.LogisticRegression(
        solver='liblinear',
        C=正则强度)
'''

import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm

# train_set
x = np.array([
        [3, 1],
        [2, 5],
        [1, 8],
        [6, 4],
        [5, 2],
        [3, 5],
        [4, 7],
        [4, -1]])                                           # 散点[x,y]
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])                      # 分类点颜色依据

# 逻辑回归模型
model = lm.LogisticRegression(solver='liblinear', C=1)
model.fit(x, y)

# test_set
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.05         # 左边界，右边界，水平方向点间距
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.05         # 下边界，上边界，垂直方向点间距

grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))    # 点阵  ????????????

flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = np.zeros(len(flat_x), dtype=int)
flat_y[flat_x[:, 0] < flat_x[:, 1]] = 1                         # 边界 ？？？？？？？？？
grid_y = flat_y.reshape(grid_x[0].shape)

plt.figure('Logistic Classification', facecolor='lightgray')
plt.title('Logistic Classification', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')       # 参数？？？？？？？？？？

plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=60)        # 颜色映射