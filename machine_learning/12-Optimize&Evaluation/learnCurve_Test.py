# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:36:32 2018

@author: Administrator
"""
'''
学习曲线:训练参数大小train_sizes
sklearn.model_selection.learning_curve(model,
                                       x,
                                       y,
                                       训练集大小数组,
                                       cv=5)
    --> return: 训练集大小数组，训练集得分矩阵，测试集得分矩阵
'''
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as plt

data = []
with open('car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))

data = np.array(data).T                     # 转置后优先行编码，相当于对原data列编码
encoders, x = [], []
for row in range(len(data)):                # 行遍历(即原数据源列遍历)，标签编码
    encoder = sp.LabelEncoder()
    encoders.append(encoder)
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))    # 前len-1行作为train_x
    else:
        y = encoder.fit_transform(data[row])          # 最后一列作为train_y

x = np.array(x).T                                     # train_x还原

# 随机森林分类器
model = se.RandomForestClassifier(max_depth=9, n_estimators=140,random_state=7)

# 训练集大小
train_sizes = np.linspace(100, 1000, 10).astype(int)
train_sizes, train_scores, test_score = ms.learning_curve(model, x, y, train_sizes=train_sizes, cv=5)
print(train_sizes, train_scores, sep='\n')
# train_sizes/ score     
#            100         [[1.         1.         1.         1.         1.        ]
#            200          [1.         1.         1.         1.         1.        ]
#            300          [1.         1.         1.         1.         1.        ]
#            400          [1.         1.         1.         1.         1.        ]
#            500          [1.         1.         1.         1.         1.        ]
#            600          [1.         1.         1.         1.         1.        ]
#            700          [1.         0.99857143 1.         1.         1.        ]
#            800          [0.99875    1.         1.         1.         1.        ]
#            900          [1.         0.99777778 0.99777778 1.         1.        ]
#            1000         [0.993      0.995      0.995      1.         1.        ]]
train_means = train_scores.mean(axis=1)               # 每一行的平均数，一行表示一个取值下的f1_score 
train_std= train_scores.std(axis=1)
test_means = test_score.mean(axis=1)
test_std = test_score.std(axis=1)
#print(train_means, train_std,test_means, test_std, sep='\n')


plt.figure('Learning Curve', facecolor='lightgray')
plt.title('Learning Curve', fontsize=14)
plt.xlabel('Train Size', fontsize=14)
plt.ylabel('f1_score', fontsize=14)
plt.tick_params(labelsize=10)

plt.fill_between(train_sizes, test_means - test_std, test_means + test_std, color='lightblue', alpha=0.25)
plt.plot(train_sizes, train_means, 'o-', c='blue', label='Training')
plt.plot(train_sizes, test_means, 'o-', c='red', label='Testing')
plt.legend()
plt.tight_layout()
plt.show()

model2 = se.RandomForestClassifier(n_estimators=140, random_state=7)
n_estimators = np.linspace(20, 200, 10).astype(int)
max_depth = np.linspace(1,10,10).astype(int)
print(max_depth)

# 生成验证曲线
train_scores1, test_score1 = ms.validation_curve(model, x, y, 'n_estimators', n_estimators, cv=5)
print(train_scores1)
train_means1 = train_scores1.mean(axis=1)               # 每一行的平均数，一行表示一个取值下的f1_score 
train_std1= train_scores1.std(axis=1)
test_means1 = test_score1.mean(axis=1)
test_std1 = test_score1.std(axis=1)

train_scores2, test_score2 = ms.validation_curve(model2, x, y, 'max_depth', max_depth, cv=5)
train_means2 = train_scores2.mean(axis=1)               # 为什么是axis=1                             ????????
train_std2= train_scores2.std(axis=1)
test_means2 = test_score2.mean(axis=1)
test_std2 = test_score2.std(axis=1)
print(test_score2)

# 绘图
plt.figure('Validation Curve', facecolor='lightgray')
plt.subplot(121)
plt.title('Validation Curve', fontsize=14)
plt.xlabel('n_estimators', fontsize=14)
plt.ylabel('f1_score', fontsize=14)
plt.tick_params(labelsize=10)

plt.fill_between(n_estimators, train_means1 - train_std1, train_means1 + train_std1, color='lightblue', alpha=0.25)
plt.fill_between(n_estimators, test_means1 - test_std1, test_means1 + test_std1, color='orangered', alpha=0.25)
plt.plot(n_estimators, train_means1, 'o-', c='blue', label='Training')
plt.plot(n_estimators, test_means1, 'o-', c='red', label='Testing')
plt.legend()
'''
f1_score 训练集分值高，但测试集分值低，说明训练模型有点儿过拟合
n_estimators=120~140较为合适，后续采用这个参数对max_depth进行验证
'''

plt.subplot(122)
plt.title('Validation Curve', fontsize=14)
plt.xlabel('max_depth', fontsize=14)
plt.tick_params(labelsize=10)

plt.fill_between(max_depth, train_means2 - train_std2, train_means2 + train_std2, color='lightblue', alpha=0.25)
plt.fill_between(max_depth, test_means2 - test_std2, test_means2 + test_std2, color='orangered', alpha=0.25)
plt.plot(max_depth, train_means2, 'o-', c='blue', label='Training')
plt.plot(max_depth, test_means2, 'o-', c='red', label='Testing')
plt.legend()

plt.tight_layout()
plt.show()

'''
plt.fill_between(水平坐标数组, 垂直坐标起点数组, 垂直坐标终点数组, 条件, color=颜色, alpha=透明度)
'''