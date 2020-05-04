# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:44:06 2018

@author: Administrator
"""

import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as plt
# import pandas as pd
'''
DBSCAN聚类：

'''
x = []
with open('perf.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)

model = sc.DBSCAN(eps=0.8,                      # 圆的半径
                  min_samples=5                 # 一个聚类中的最少样本数
                  )

pred_y = model.fit_predict(x)                   # 模型训练和预测一起完成
core_mask = np.zeros(len(x), dtype=bool)        # 核心样本初始化，全部0，都不是核心样本，后续通过掩码过滤出核心样本
core_mask[model.core_sample_indices_] = True    # 核心样本索引掩码
offset_mask = model.labels_ == -1               # 类的标签值为-1的是 偏离样本
'TODO: 取反获取外围样本 逻辑运算, ~:非, |:或'
periphery_mask = ~(core_mask | offset_mask)     # 取反 numpy的逻辑运算，即 外周样本  <------ 留意获取外围样本的方式
print(periphery_mask, '---')

labels = set(pred_y)
# print(labels)                                   # {0, 1, 2, 3, 4, -1}

'TODO: 分别获取 核心样本, 外围样本, 偏离样本'
core_samples = x[model.core_sample_indices_]
periphery_samples = x[periphery_mask]
outer_samples = x[offset_mask]
print(core_samples.shape, periphery_samples.shape, outer_samples.shape)

# 获取所有样本并打标签
print(x.shape, pred_y.shape)
labeled_sample = np.hstack((x, pred_y.reshape((-1, 1))))
# print(labeled_sample.shape, '----')

# # 获取偏离点  : 采用 np.take 和 np.where
# outers = np.take(labeled_sample, np.where(labeled_sample[:, -1] == -1), axis=0)[0, :, :]
# print(outers, 'outers----------')
# # 获取偏离点 : 采用 掩码 mask
# outerss = x[offset_mask]
# print(outerss)

plt.figure('DBSCAN Clustering', facecolor='lightgray')
plt.title('DBSCAN Clustering', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

color_s = plt.get_cmap('brg', len(labels))(range(len(labels)))  # 把brg颜色映射等分为len(labels)份
print(color_s)
# [[0.  0.  1.  1. ]              # 一行表示一种颜色
# [0.4 0.  0.6 1. ]
# [0.8 0.  0.2 1. ]
# [0.8 0.2 0.  1. ]
# [0.4 0.6 0.  1. ]
# [0.  1.  0.  1. ]]

# plt.scatter(core_mask[:, 0], core_mask[:, 1], c=color_s, cmap='brg', s=30)
plt.scatter(x[core_mask][:, 0], x[core_mask][:, 1],
            c=color_s[pred_y[core_mask]],
            s=30,
            label='core')

plt.scatter(x[periphery_mask][:, 0], x[periphery_mask][:, 1], c=color_s[pred_y[periphery_mask]],
            s=30, label='periphery', facecolor='none', marker='^')
plt.scatter(x[offset_mask][:, 0], x[offset_mask][:, 1], c=color_s[pred_y[offset_mask]], s=30, label='offset', marker='x')

plt.show()
