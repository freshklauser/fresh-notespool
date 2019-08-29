# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:45:50 2018

@author: Administrator
"""
'''
划分训练集和测试集
sklearn.model_selection.train_test_split(输入集合, 
                                         输出集合, 
                                         test_size=测试集占比, 
                                         random_state=随机种子源)
    --> return：train_x, test_x, train_y, test_y
代码：dataSplit.py

交叉验证（评估模型性能）：
1）查准率和召回率综合：
f1_score = 2*查准率*召回率 / (查准率+召回率)
sklearn.model_selection.cross_val_score(分类器,
                                        输入集合,
                                        输出集合,
                                        cv =验证次数,
                                        scoring=验证指标名称)
    --> return:验证指标值数组(size=cv)
'''
import numpy as np
import matplotlib.pyplot as plt
import sklearn.naive_bayes as nb                # 朴素贝叶斯
import sklearn.model_selection as ms

# train_set
x, y = [], []
with open('multiple1.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)



# 数据集
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)


# 朴素贝叶斯模型多元分类: 计算概率用的是高斯分布进行密度计算

# 选择模型
model = nb.GaussianNB()

# 评估模型性能：交叉验证f1_score （预测之前就可以直接评估模型）
val_cross = ms.cross_val_score(model, train_x, train_y, cv=4, scoring='f1_weighted').mean()         # f1_score
#val_cross = ms.cross_val_score(model, train_x, train_y, cv=4, scoring='precision_weighted').mean()  # 查准率
#val_cross = ms.cross_val_score(model, train_x, train_y, cv=4, scoring='recall_weighted').mean()     # 召回率

# 模型训练和预测
model.fit(train_x, train_y)                 # 训练数据集
pred_test_y = model.predict(test_x)         # 测试数据集




# 边界
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005           # 左边界，右边界，水平方向点间距
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005           # 下边界，上边界，垂直方向点间距

# 栅格化：pcolormap参数
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))    # (m-array,n-array)--> list(mat(m,n), mat(m,n))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]            # 保证输入散点的坐标点横纵坐标个数一样
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

plt.figure('Naive Bayes Classification', facecolor='lightgray')
plt.title('Naive Bayes Classification', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')       # 参数
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=40)            # 颜色映射
plt.show()