# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:44:06 2018

@author: Administrator
"""
'''
agglo聚类：凝聚层次
在空间上具有明显连续性方向，但彼此间的距离未必最近的样本
'''
import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as snb           # 找临近点
import matplotlib.pyplot as plt

n_samples = 500
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_samples, 1))    # (500, 1)
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_samples, 2)                     # (500, 1)
x = np.hstack((x, y)) + n
#print(x)

model_nonc = sc.AgglomerativeClustering(linkage='average',
                                        n_clusters=3
                                        )
pred_y_nonc = model_nonc.fit_predict(x)           # 训练和预测一起完成, 没有center属性 没有pcolormesh边界


# 连续性样本在连续性方向上的聚类：connectivity=conn
# 找临近点
conn = snb.kneighbors_graph(x, 10, include_self='False')        # 找不含自己的10个近邻
model_conn = sc.AgglomerativeClustering(linkage='average',
                                        n_clusters=10,
                                        connectivity=conn       # 连续性
                                        )
pred_y_conn = model_conn.fit_predict(x)

plt.figure('AgglomerativeClustering', facecolor='lightgray')
plt.subplot(121)
plt.title('NoneConnectivity', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)
plt.scatter(x[:, 0], x[:, 1], c=pred_y_nonc, cmap='brg', s=30)

plt.subplot(122)
plt.title('Connectivity', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)
plt.scatter(x[:, 0], x[:, 1], c=pred_y_conn, cmap='brg', s=30)

plt.show()
