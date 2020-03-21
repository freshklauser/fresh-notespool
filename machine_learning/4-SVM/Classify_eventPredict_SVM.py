# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:23:11 2018

@author: Administrator
"""
'''
SVM应用案例：分类
'''

import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as plt

# 自定义编码器：数字编码
class DigitEncoder():
    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)

data = []
with open('event.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.delete(np.array(data).T, 1, 0)        # 删除axis=0即行，rowidex=1即第二行的数据
print('data[:,-1]:',data[-1,:])                 # 转置后的最后一列
encoders, x = [], []
for row in range(len(data)):
#    print(data[2,0])
    if data[row, 0].isdigit():          # 数字，用自定义的encoder
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()     # 非数字，用sp的标签编码器
    if row < len(data) - 1:             # 前n-1行 x, 最后一行y
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])            # y: <class 'numpy.ndarray'>
    encoders.append(encoder)
x = np.array(x).T
print('x[5,:]:', x[:5,:], sep='\n', end='\n\n')
print('y:', y[:10])                                     # y: [1 1 1 1 1 1 1 1 1 1]

train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)
model = svm.SVC(kernel='rbf', class_weight='balanced')
# 交叉验证评估模型：测试f1_score
print('f1_score:',ms.cross_val_score(model, x, y, cv=3, scoring='f1_weighted').mean())
# 0.938166292765643 fi_score可以，采用该参数组训练模型

model.fit(train_x, train_y)                     # 训练集训练模型
pred_test_y = model.predict(test_x)             # 测试集测试模型
# test_set分类结果：如何确定0类和1类分别是代表
print('pred_test_y:',pred_test_y[:10])                 # pred_test_y: [1 1 1 1 1 1 1 1 1 1]

# 模型效果评估
print((pred_test_y == test_y).sum() / pred_test_y.size)         # 查准率
print(sm.confusion_matrix(test_y, pred_test_y))                 # 混淆矩阵 参数(实际输出，预测输出)
print(sm.classification_report(test_y, pred_test_y))            # 分类报告 参数(实际输出，预测输出)

# 根据输入数据利用SVM模型进行分类预测
data = [['Tuesday','12:30:00','21','23']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))                      # 使用已有的编码器
x = np.array(x).T
pred_y = model.predict(x)
output_y = encoders[-1].inverse_transform(pred_y)               # 解码
print('pred_y:', pred_y)                                        # pred_y: [1]
print('output_y:', output_y)                                    # output_y: ['noevent']