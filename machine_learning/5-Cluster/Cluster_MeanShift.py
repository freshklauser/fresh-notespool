# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:44:06 2018

@author: Administrator
"""
'''
均值漂移聚类
'''
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as plt

x = []
with open('multiple3.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)

bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.1)  # 带宽 直方图的宽度  quantile越大 带宽越大
# 模型k-means
model = sc.MeanShift(bandwidth=bw,              # 密度函数对应的直方图的带宽
                     bin_seeding=True           # 尽量让少样本的聚类与其他聚类合并
                     )                          # n_cluster不需要，自己会确定聚类数
model.fit(x)

# 获取聚类中心
centers = model.cluster_centers_
print('centers:',centers, sep='\n')
#[[1.86416667 2.03333333]
# [6.87444444 5.57638889]
# [3.45088235 5.27323529]
# [5.90964286 2.40357143]
# [6.36083333 3.8475    ]
# [4.26333333 1.51833333]]

plt.figure('MeanShift Cluster', facecolor='lightgray')
plt.title('MeanShift Cluster', fontsize=14)
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
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v)) # 栅格点阵
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
