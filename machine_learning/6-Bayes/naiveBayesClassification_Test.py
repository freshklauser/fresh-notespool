# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:26:26 2018

@author: Administrator
"""
'''
朴素贝叶斯分类器
'''

import numpy as np
import matplotlib.pyplot as plt
import sklearn.naive_bayes as nb                # 朴素贝叶斯

# train_set
x, y = [], []
with open('multiple1.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)

# 计算概率用的是高斯分布进行密度计算
model = nb.GaussianNB()                                         # 朴素贝叶斯分类器
model.fit(x, y)

l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005           # 左边界，右边界，水平方向点间距
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005           # 下边界，上边界，垂直方向点间距

# 栅格化
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))    # (m-array,n-array)--> list(mat(m,n), mat(m,n))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]            # 保证输入散点的坐标点横纵坐标个数一样
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

plt.figure('Naive Bayes Classification', facecolor='lightgray')
plt.title('Naive Bayes Classification', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')       # 参数
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=40)            # 颜色映射
plt.show()