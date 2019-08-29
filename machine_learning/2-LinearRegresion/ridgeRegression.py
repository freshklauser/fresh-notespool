# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:56:50 2018

@author: Administrator
"""

import pickle                              # 硬盘存储模块
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm               # ??? 干嘛的？？
import matplotlib.pyplot as plt
import sklearn.pipeline as spp

# 数据预处理
x, y = [], []
# 读取文件
with open('abnormal.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)
#print(x.shape, y.shape)

'''
模型建立
sklearn.linear_model.LinearRegression()
    --> return：线性回归器
                线性回归器.fit(输入样本，输出标签)              # 训练数据
                线性回归器.predict(输入样本)                    # 预测数据
                    -- > return：预测输出标签
'''
model_ln = lm.LinearRegression()               # 构建线性回归器
model_ln.fit(x, y)                             # 不返回k和b model中存储
pred_y_ln = model_ln.predict(x)

'''
岭回归 (削弱异常值对拟合的影响,正则强度越大，削弱的越厉害，降低对异常数据的依赖)
loss = J(k, b) + 正则函数(样本权重)*正则强度(或惩罚系数）
sklearn.linear_model.Ridge(正则强度,                        # 削弱异常值影响，避免过拟合？？ 值如何选定？？
                           fit_intercept=是否修正截距，
                           max_iter=最大迭代次数)
    --> return：岭回归器
                岭回归器.fit()              # 训练数据
                岭回归器.predict()          # 预测数据
'''
model_rd = lm.Ridge(150, fit_intercept=True, max_iter=10000)     # 构建线性回归器
model_rd.fit(x, y)                             # 不返回k和b model中存储
pred_y_rd = model_rd.predict(x)

'''
多项式回归
sklearn.preprocessing.PolynomialFeatures(最高次数)
    --> return：多项式特征扩展器
sklearn.pipeline.make_pipe(多项式特征扩展器, 线性回归器)              # 管线函数
    --> return：参数k1,k2,k3...
x-->多项式特征扩展器 -- x x^2 x^3 ... --> 线性回归器 ---> k1,k2,k3...
'''

# 评估模型
print(sm.mean_absolute_error(y, pred_y_ln))        # 平均误差
print(sm.mean_squared_error(y, pred_y_ln))         # 平均方差
print(sm.median_absolute_error(y, pred_y_ln))      # 
print(sm.r2_score(y, pred_y_ln))                   # LR模型推荐使用sm.r2_score评估

# 模型写入硬盘 pkl格式 方便pickle模块读取
with open('linear.pkl', 'wb') as f:
    pickle.dump(model_ln, f)
with open('ridge.pkl', 'wb') as f:
    pickle.dump(model_rd, f)
    

'''
可视化
'''
plt.figure('Ridge Regression', facecolor='lightgray')
plt.title('Ridge Regression', fontsize=20)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
# 输入样本散点图
plt.scatter(x, y, label='Sample', color='black',linewidth=1,alpha=1)
# predict图
print(x)
sorted_indices = x.T[0].argsort()           # ???
print(sorted_indices)

plt.plot(x[sorted_indices], pred_y_ln[sorted_indices], 'o-', label='LinearRegression', color='r',linewidth=1,alpha=1)
plt.plot(x[sorted_indices], pred_y_rd[sorted_indices], 'o-', label='RidgeRegression', color='g',linewidth=1,alpha=1)

plt.legend(fontsize=8, loc='upper left')
plt.show()






'''
def r2_score(y_true, y_pred, sample_weight=None,
             multioutput="uniform_average"):
    """R^2 (coefficient of determination) regression score function.

    Best possible score is 1.0 and it can be negative (because the
    model can be arbitrarily worse). A constant model that always
    predicts the expected value of y, disregarding the input features,
    would get a R^2 score of 0.0.
'''