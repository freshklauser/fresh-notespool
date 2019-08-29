# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:05:47 2018

@author: Administrator
"""
'''
获取特征重要性序列
'''

import numpy as np
import sklearn.datasets as sd           # 数据包
import sklearn.utils as su              # 小工具包
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm            # 评估模型效果
import matplotlib.pyplot as plt
'''
The :mod:`sklearn.ensemble` module includes ensemble-based methods for
classification, regression and anomaly detection.
'''


# 获取标准数据集
housing = sd.load_boston()              # 自带数据集,<class 'sklearn.utils.Bunch'>

features_names = housing.feature_names  # 获取特征名
#['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']

print(housing.data.shape)               # (506, 13)
print(housing.target.shape)             # 目标：预测的房价

# trainning_set, testing_set
x, y = su.shuffle(housing.data, housing.target,random_state=7)   # 打乱数据顺序
train_size = int(len(x) * 0.8)                                   # 数据集的80%作为训练集, 20%作为测试集
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]


# 决策树模型
model = st.DecisionTreeRegressor(max_depth=5)       # 最大树高4层
model.fit(train_x, train_y)                         # 训练模型
pred_test_y = model.predict(test_x)                 # 模型预测值 若==test_y，则完全吻合
'''
# 获取决策树模型计算得到的特征重要性序列,返回的不是特征名称，是特征重要性评估值
'''
fi_dt = model.feature_importances_
#[0.03955725 0.         0.         0.         0.03188556 0.59944603...]



# 基于决策树的正向激励 （元回归器 == 决策树回归器）
model = se.AdaBoostRegressor(st.DecisionTreeRegressor(max_depth=5),     # 元回归器
                             n_estimators=400,                          # 评估器数b
                             random_state=7                             # 随机种子源
                             )
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
'''
# 获取决策树模型计算得到的特征重要性序列,返回的不是特征名称，是特征重要性评估值
'''
fi_dt = model.feature_importances_


# 绘图：特征重要性排序图
plt.figure('Feature Importance', facecolor='lightgray')
plt.subplot(211)
plt.title('DecisionTreeRegressor', fontsize=14)
plt.ylabel('Importance', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(axis='y', linestyle=':')
sorted_indices = fi_dt.argsort()[::-1]                     # 以fi_dt值为参考间接对index排序,并按index降序
# argsort函数返回的是序列值从小到大的索引值
pos = np.arange(sorted_indices.size)
plt.bar(pos, fi_dt[sorted_indices],facecolor='deepskyblue', edgecolor='steelblue')
plt.xticks(pos, features_names[sorted_indices], rotation=30)    # 刻度

plt.subplot(212)
plt.title('AdaBoostRegressor', fontsize=14)
plt.ylabel('Importance', fontsize=12)
plt.tick_params(labelsize=10)
plt.grid(axis='y', linestyle=':')
sorted_indices = fi_ab.argsort()[::-1]                     # 以fi_dt值为参考间接对index排序,并降序
pos = np.arange(sorted_indices.size)
plt.bar(pos, fi_ab[sorted_indices],facecolor='lightcoral', edgecolor='indianred')
plt.xticks(pos, features_names[sorted_indices], rotation=30)

plt.tight_layout()
plt.show()

