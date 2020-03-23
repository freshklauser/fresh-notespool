# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:12:18 2018

@author: Administrator
"""
'''
多元分类：逻辑回归分类器
sklearn.linear_model.LogisticRegression(
        solver='liblinear',
        C=正则强度)
'''

import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm

# train_set
x = np.array([
        [4, 7],
        [3.5, 8],
        [3.1, 6.2],
        [0.5, 1],
        [1, 2],
        [1.2, 1.9],
        [4, 2],
        [5.7, 1.5],
        [5.4, 2.2]])                                            # 散点[x,y]
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])                       # 多元分类 3类

# 逻辑回归分类器
model = lm.LogisticRegression(solver='liblinear', C=50)         # C
model.fit(x, y)

# test_set
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005           # 左边界，右边界，水平方向点间距
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005           # 下边界，上边界，垂直方向点间距

#print(np.arange(l, r, h).shape, np.arange(b, t, v).shape)       # (1440,) (1800,),shape不同，不能直接作为输入,转为
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))     # (m-array,n-array)--> list(mat(m,n), mat(m,n))
#print(grid_x)                                                   # list
print(grid_x[0])
print(grid_x[1])                                          # (1800, 1440) <class 'numpy.ndarray'>
#print(grid_x[1].shape)                                          # (1800, 1440) <class 'numpy.ndarray'>

flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]            # 保证输入散点的坐标点横纵坐标个数一样
flat_y = model.predict(flat_x)

grid_y = flat_y.reshape(grid_x[0].shape)

plt.figure('Logistic Classification', facecolor='lightgray')
plt.title('Logistic Classification', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

# pcolormesh: 伪彩图 pcolormesh(X, Y, C)
# X,Y均为2-D array,如果为1-D 会自动广播，X和Y构成网格点阵
# X,Y对应位置元素x[i,j]和y[i,j]组成一个坐标点(x[i,j],y[i,j])，对样本周围（包括样本所在坐标）的四
#个坐标点进行着色，C代表着色方案
plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')\


plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=60)            # 颜色映射