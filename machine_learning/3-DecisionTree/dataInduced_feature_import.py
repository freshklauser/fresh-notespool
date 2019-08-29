# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:05:47 2018

@author: Administrator
"""

'''
决策树：
sklearn.tree.DecisionTreeRegressor()
    --> 决策树回归器
    
正向激励
sklearn.ensemble.AdaBoostRegressor(元回归器，
                                   n_estimators=评估器数，
                                   random_state=随机种子源)
    --> 正向激励回归器
    
随机森林
sklearn.ensemble.RandomForestRegressor(max_depth=最大树高,
                                       n_estimators=评估器数 b,
                                       min_samples_split=划分子表的最小样本数)
    --> 随机森林回归器
代码：houseDecisionTree.py

决策树模型.feature_importances_ ： 特征重要性(根据训练过程中信息熵的计算得到的)
代码：feature_import.py
'''

import csv
import numpy as np
import sklearn.utils as su              # 小工具包
import sklearn.ensemble as se   
import sklearn.metrics as sm            # 评估模型效果
import matplotlib.pyplot as plt

with open('bike_day.csv', 'r') as f:
    reader = csv.reader(f)                       # csv文件读取器, 迭代一次是一行，行内以逗号分隔
    x, y = [], []
    for row in reader:
        x.append(row[2:13])                     # 2~12列, 每一行作为一个list, list切片后append到x中，最后np.array 
        y.append(row[-1])                       # 最后一列

feature_name = np.array(x[0])                   # 第一行 
x = np.array(x[1:], dtype=float)
y = np.array(y[1:], dtype=float)
print(x.shape, y.shape)


# trainning_set, testing_set
x, y = su.shuffle(x, y,random_state=7)   # 打乱数据顺序
train_size = int(len(x) * 0.9)          # 数据集的80%作为训练集, 20%作为测试集
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]


# 随机森林模型
model = se.RandomForestRegressor(max_depth=10,
                                 n_estimators=1000,
                                 min_samples_split=2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
'''
# 获取决策树模型计算得到的特征重要性序列,返回的不是特征名称，是特征重要性评估值
'''
fi_dy = model.feature_importances_

print(sm.r2_score(test_y, pred_test_y))         # 0.891422378122565

# **************************************************************************************************

with open('bike_hour.csv', 'r') as f:
    reader = csv.reader(f)                       # csv文件读取器, 迭代一次是一行，行内以逗号分隔
    x, y = [], []
    for row in reader:
        x.append(row[2:13])                     # 2~12列, list切片
        y.append(row[-1])                       # 最后一类

feature_name = np.array(x[0])                   # 第一行
x = np.array(x[1:], dtype=float)
y = np.array(y[1:], dtype=float)
print(x.shape, y.shape)


# trainning_set, testing_set
x, y = su.shuffle(x, y,random_state=7)   # 打乱数据顺序
train_size = int(len(x) * 0.9)          # 数据集的80%作为训练集, 20%作为测试集
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]

model = se.RandomForestRegressor(max_depth=10,
                                 n_estimators=1000,
                                 min_samples_split=2)
model.fit(train_x, train_y)
'''
# 获取决策树模型计算得到的特征重要性序列,返回的不是特征名称，是特征重要性评估值
'''
fi_hr = model.feature_importances_

pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))         # 0.891422378122565

plt.figure('Feature Importance', facecolor='lightgray')
plt.subplot(211)
plt.title('Bike of Day', fontsize=14)
plt.ylabel('Importance', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(axis='y', linestyle=':')
sorted_indices = fi_dy.argsort()[::-1]                     # 以fi_dt值为参考间接对index排序,并降序
pos = np.arange(sorted_indices.size)
plt.bar(pos, fi_dy[sorted_indices],facecolor='deepskyblue', edgecolor='steelblue')
plt.xticks(pos, feature_name[sorted_indices], rotation=30)    # 刻度

plt.subplot(212)
plt.title('Bike of Hour', fontsize=14)
plt.ylabel('Importance', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(axis='y', linestyle=':')
sorted_indices = fi_hr.argsort()[::-1]                     # 以fi_dt值为参考间接对index排序,并降序
pos = np.arange(sorted_indices.size)
plt.bar(pos, fi_hr[sorted_indices],facecolor='lightcoral', edgecolor='indianred')
plt.xticks(pos, feature_name[sorted_indices], rotation=30)

plt.tight_layout()
plt.show()

