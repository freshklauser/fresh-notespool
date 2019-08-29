# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:23:11 2018

@author: Administrator
"""
'''
SVM分类:最优超参数
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

train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)

# 最优超参数组合列表
params = [
        {'kernel': ['linear'], 'C': [1, 10, 100, 100]},
        {'kernel': ['poly'], 'C': [1], 'degree': [2, 3]},
        {'kernel': ['rbf'], 'C': [1, 10, 100, 100], 'gamma':[1, 0.1, 0.01, 0.001]}
        ]

model = ms.GridSearchCV(svm.SVC(probability=True), params, cv=5)     # 返回的就是最优的超参数组合
model.fit(train_x, train_y)

# 获取超参数得分 model.cv_results_['mean_test_score']   遍历for 
# model.cv_results_['mean_test_score'] 与 model.cv_results_['params']对应数据的平均值
for param, score in zip(model.cv_results_['params'],model.cv_results_['mean_test_score']): 
    print(param, score)
    #{'C': 1, 'kernel': 'linear'} 0.6577777777777778
    # ...
    #{'C': 1, 'gamma': 1, 'kernel': 'rbf'} 0.9511111111111111
    # ...

# 打印最优参数组合 model.best_params_
print(model.best_params_)       # {'C': 1, 'gamma': 1, 'kernel': 'rbf'}


l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005

grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))

flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)

grid_y = flat_y.reshape(grid_x[0].shape)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y, pred_test_y))

prob_x = np.array([[2, 1.5],[8, 9], [4.8, 5.2], [4,4],[2.5,7],[7.6,2],[5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)

plt.figure('The Best HyperParametre', facecolor='lightgray')
plt.title('The Best Hyperparametre', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)


plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
c0, c1 = y==0, y==1                                                         # 掩码
plt.scatter(x[c0][:, 0], x[c0][:, 1], c='b', s=30)
plt.scatter(x[c1][:, 0], x[c1][:, 1], c='r', s=30)
C0, C1 = pred_prob_y==0, pred_prob_y==1
plt.scatter(prob_x[C0][:, 0], prob_x[C0][:, 1], c='y', s=30, marker='D')
plt.scatter(prob_x[C1][:, 0], prob_x[C1][:, 1], c='purple', s=30, marker='D')

for i in range(len(probs[C0])):
    plt.annotate(
            '{}% {}%'.format(round(probs[C0][:, 0][i],2)*100, round(probs[C0][:, 1][i],2)*100),
            xy=(prob_x[C0][:, 0][i], prob_x[C0][:, 1][i]),                  # 点坐标
            xytext=(12, -12),textcoords='offset points',
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=9,
            bbox={'boxstyle':'round, pad=0.6','fc':'deepskyblue', 'alpha':0.4})

for i in range(len(probs[C1])):
    plt.annotate(
            '{}% {}%'.format(round(probs[C1][:, 0][i], 2)*100, round(probs[C1][:, 1][i], 2)*100),
            xy=(prob_x[C1][:, 0][i], prob_x[C1][:, 1][i]),
            xytext=(12, -12),textcoords='offset points',
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=9,
            bbox={'boxstyle':'round, pad=0.6','fc':'green', 'alpha':0.4})

plt.show()


'''
class SVC(sklearn.svm.base.BaseSVC)
    C-Support Vector Classification.
 
    C : float, optional (default=1.0)
        Penalty parameter C of the error term.
    kernel : string, optional (default='rbf')
         Specifies the kernel type to be used in the algorithm.
         It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or
         a callable.
         If none is given, 'rbf' will be used. If a callable is given it is
         used to precompute the kernel matrix.
    degree : int, optional (default=3)
        Degree of the polynomial kernel function ('poly').
        Ignored by all other kernels.
    gamma : float, optional (default='auto')
        Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.
        If gamma is 'auto' then 1/n_features will be used instead.
    probability : boolean, optional (default=False)
        Whether to enable probability estimates. This must be enabled prior
        to calling `fit`, and will slow down that method.
    class_weight : {dict, 'balanced'}, optional
        Set the parameter C of class i to class_weight[i]*C for
        SVC. If not given, all classes are supposed to have
        weight one.
        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``
'''