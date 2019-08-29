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

# 数据预处理
x, y = [], []
# 读取文件
with open('single.txt', 'r') as f:
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
                线性回归器.fit(输入样本，输出标签)
                线性回归器.predict(输入样本)
                    -- > return：预测输出标签
'''
model = lm.LinearRegression()               # 构建线性回归器
model.fit(x, y)                             # 不返回k和b model中存储
pred_y = model.predict(x)

# 评估模型
print(sm.mean_absolute_error(y, pred_y))        # 平均误差
print(sm.mean_squared_error(y, pred_y))         # 平均方差
print(sm.median_absolute_error(y, pred_y))      # 
print(sm.r2_score(y, pred_y))                   # LR模型推荐使用sm.r2_score评估

# 模型写入硬盘 pkl格式 方便pickle模块读取
with open('linear.pkl', 'wb') as f:
    pickle.dump(model, f)

'''
可视化
'''
plt.figure('Linear Regression', facecolor='lightgray')
plt.title('Linear Regression', fontsize=20)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
# 输入样本散点图
plt.scatter(x, y, label='Sample', color='black',linewidth=1,alpha=1)
# predict图
sorted_indices = x.T[0].argsort()           # ???
plt.plot(x[sorted_indices], pred_y[sorted_indices], 'o-', label='LR', color='r',linewidth=1,alpha=1)

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