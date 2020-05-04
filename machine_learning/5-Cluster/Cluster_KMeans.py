# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:44:06 2018

@author: Administrator
"""

import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as plt

'''
k均值聚类
'''

x = []
with open('multiple3.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)

# 模型k-means
model = sc.KMeans(init='k-means++',         # 初始化中心
                  n_clusters=4)             # 聚类数
model.fit(x)

# 获取聚类中心
centers = model.cluster_centers_

plt.figure('K-means Cluster', facecolor='lightgray')
plt.title('K-means Cluster', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

'''
plt.pcolormesh()
'''
# 点阵
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
# 栅格化
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))  # 栅格点阵
# 平面化
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]         # 栅格横坐标拉平成1维，预测一维栅格分类值
flat_y = model.predict(flat_x)                               # 一维栅格分类值(作为颜色区分pcolormesh的c)
grid_y = flat_y.reshape(grid_x[0].shape)                     # 栅格分类reshape与grid_x一样
# 绘制分类边界 pcolormesh 水平坐标，垂直坐标，颜色，颜色映射
plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='binary')

'''
绘图
'''
pred_y = model.predict(x)
plt.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=30)
plt.scatter(centers[:, 0], centers[:, 1], marker='+', c='gold', s=40)

plt.show()
