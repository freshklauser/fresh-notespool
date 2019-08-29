# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:23:11 2018

@author: Administrator
"""
'''
SVM:支持向量机的线性分类 
'''

import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as plt

x, y = [], []
with open('multiple2.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)
#print(y)
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)

model = svm.SVC(kernel='rbf', C=600, gamma=0.01, probability=True)
'''
    kernel : string, optional (default='rbf')
         Specifies the kernel type to be used in the algorithm.
         It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or
         a callable.
         If none is given, 'rbf' will be used. If a callable is given it is
         used to precompute the kernel matrix.

    degree : int, optional (default=3)
        Degree of the polynomial kernel function ('poly').
        Ignored by all other kernels.
'''
model.fit(train_x, train_y)

# 点阵
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005

# 栅格化
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))

# 平面化
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]              # 点阵中每个点的水平坐标和垂直坐标
#print(flat_x)
flat_y = model.predict(flat_x)
#print(flat_y)

# 平面--》栅格点阵
grid_y = flat_y.reshape(grid_x[0].shape)
#print(grid_y)

pred_test_y = model.predict(test_x)
#print(sm.classification_report(test_y, pred_test_y))

prob_x = np.array([[2, 1.5],[8, 9], [4.8, 5.2], [4,4],[2.5,7],[7.6,2],[5.4, 5.9]])
#print(prob_x)
pred_prob_y = model.predict(prob_x)
#print(pred_prob_y)
probs = model.predict_proba(prob_x)
#print(probs)



plt.figure('SVM RBF Classification', facecolor='lightgray')
plt.title('SVM RBF Classification', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

# 绘制分类边界 pcolormesh 水平坐标，垂直坐标，颜色，颜色映射
plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
c0, c1 = y==0, y==1         # 掩码
plt.scatter(x[c0][:, 0], x[c0][:, 1], c='b', s=30)
plt.scatter(x[c1][:, 0], x[c1][:, 1], c='r', s=30)
C0, C1 = pred_prob_y==0, pred_prob_y==1
plt.scatter(prob_x[C0][:, 0], prob_x[C0][:, 1], c='y', s=30, marker='D')
plt.scatter(prob_x[C1][:, 0], prob_x[C1][:, 1], c='purple', s=30, marker='D')

for i in range(len(probs[C0])):
    plt.annotate(
            '{}% {}%'.format(round(probs[C0][:, 0][i],2)*100, round(probs[C0][:, 1][i],2)*100),
            xy=(prob_x[C0][:, 0][i], prob_x[C0][:, 1][i]),
            xytext=(12, -12),textcoords='offset points',
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=9,
            bbox={'boxstyle':'round, pad=0.6','fc':'deepskyblue', 'alpha':0.8})

for i in range(len(probs[C1])):
    plt.annotate(
            '{}% {}%'.format(round(probs[C1][:, 0][i],2)*100, round(probs[C1][:, 1][i],2)*100),
            xy=(prob_x[C1][:, 0][i], prob_x[C1][:, 1][i]),
            xytext=(12, -12),textcoords='offset points',
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=9,
            bbox={'boxstyle':'round, pad=0.6','fc':'violet', 'alpha':0.8})

plt.show()