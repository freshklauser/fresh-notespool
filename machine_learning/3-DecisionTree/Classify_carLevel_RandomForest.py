# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:36:32 2018

@author: Administrator
"""
'''
随机森林分类器 评估汽车档次

'''
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

data = []
with open('car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))

data = np.array(data).T                     # 转置后优先行编码，相当于对原data列编码
encoders, train_x = [], []
for row in range(len(data)):                # 行遍历(即原数据源列遍历)，标签编码
    encoder = sp.LabelEncoder()
    encoders.append(encoder)
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))    # 前len-1行作为train_x
    else:
        train_y = encoder.fit_transform(data[row])          # 最后一列作为train_y

train_x = np.array(train_x).T                               # train_x还原

# 随机森林分类器
model = se.RandomForestClassifier(max_depth=8, n_estimators=200, random_state=7)

# 交叉验证：评估模型性能
print(ms.cross_val_score(model, train_x, train_y, cv=2, scoring='f1_weighted').mean())

# 训练模型
model.fit(train_x, train_y)

# 给定一组新数据进行分类
data = [['high','med','5more','4','big','low','unacc'],
        ['high','high','4','4','med','med','acc'],
        ['low','low','2','4','small','high','good'],
        ['low','med','3','4','med','high','vgood']]
data = np.array(data).T                                     # 转置后优先行编码，相当于对原data列编码
test_x = []
for row in range(len(data)):                                # 行遍历(即原数据源列遍历)，标签编码
    encoder = encoders[row]
    if row < len(data) - 1:
        test_x.append(encoder.transform(data[row]))         # 前len-1行作为train_x,用原编码字典
    else:
        test_y = encoder.transform(data[row])               # 最后一列作为train_y

test_x = np.array(test_x).T                                 # train_x还原
print(test_x.shape)                                         # (4, 6)
print(test_x)                                               # 标签编码后的test_x
#[[0 2 3 1 0 1]
# [0 0 2 1 1 2]
# [1 1 0 1 2 0]
# [1 2 1 1 1 0]]

# 预测
pred_test_y= model.predict(test_x)
print(pred_test_y)                                          # 标签编码后的pred_test_y[2 0 1 3]
# 标签解码
print(encoders[-1].inverse_transform(pred_test_y))          # ['unacc' 'acc' 'good' 'vgood']
