# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:44:06 2018

@author: Administrator
"""

import numpy as np
# import sklearn.preprocessing as sp
# import sklearn.model_selection as ms
# import sklearn.svm as svm
# import sklearn.metrics as sm
import sklearn.cluster as sc
import matplotlib.pyplot as plt

'''
agglo聚类：凝聚层次
基于距离而非连续性方向的聚类
对一些在空间上具有明显连续性，但彼此间的距离未必最近的样本，可以优先聚集
'''

x = []
with open('multiple3.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)

# 模型 AgglomerativeClustering
model = sc.AgglomerativeClustering(n_clusters=4)
pred_y = model.fit_predict(x)           # 训练和预测一起完成, 没有center属性 没有pcolormesh边界

plt.figure('Agglo Cluster', facecolor='lightgray')
plt.title('Agglo Cluster', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

'''
绘图
'''
plt.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=30)

plt.show()
