# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:36:32 2018

@author: Administrator
"""
'''
验证曲线validation_curve
klearn.model_selection.validation_curve(model,
                                         x,
                                         y,
                                         'n_estimators',
                                         [100, 200, 300, ...],
                                         cv=5)
    --> return:
        1   2   3   4   5  （交叉验证次数）
100 --> 0.7 0.9 .6 0.8 0.7
200 -->
300 -->
...
生成train_score和test_score后绘制曲线，结合训练集和测试集的曲线，确定较佳的参数选择。
通常，训练集得分很高，测试集得分很低，说明模型过拟合，即训练集特征匹配很好，
但不太适合测试集，模型不够泛化
def validation_curve(estimator, X, y, param_name, param_range, groups=None,
                     cv=None, scoring=None, n_jobs=1, pre_dispatch="all",
                     verbose=0):
    param_name : string
        Name of the parameter that will be varied.
    param_range : array-like, shape (n_values,)
        The values of the parameter that will be evaluated.
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
model = se.RandomForestClassifier(max_depth=8, random_state=7)
model2 = se.RandomForestClassifier(n_estimators=140, random_state=7)
n_estimators = np.linspace(20, 200, 10).astype(int)
#print(n_estimators)
max_depth = np.linspace(1,10,10).astype(int)


# 生成验证曲线
train_scores1, test_score1 = ms.validation_curve(model, x, y, 'n_estimators', n_estimators, cv=5)
print(type(train_scores1), test_score1)
#traub_scores1 cv   1            2          3         4           5
# n_estimators
#     20      [[0.97467438 0.96743849 0.96888567 0.97829233 0.96820809]   
#     40       [0.97684515 0.97105644 0.97033285 0.98552822 0.97037572]
#     60       [0.97684515 0.97467438 0.97467438 0.98480463 0.97254335]
#     80       [0.97829233 0.97322721 0.9739508  0.98408104 0.97760116]
#    100       [0.97612156 0.97684515 0.97467438 0.98480463 0.97687861]
#    120       [0.97539797 0.97684515 0.97612156 0.98552822 0.97976879]
#    140       [0.9739508  0.97612156 0.97612156 0.98625181 0.97976879]
#    160       [0.97322721 0.97539797 0.97756874 0.98408104 0.9783237 ]
#    180       [0.97322721 0.97322721 0.97612156 0.98408104 0.97904624]
#    200       [0.97322721 0.97612156 0.97539797 0.98552822 0.97760116]]

train_means1 = train_scores1.mean(axis=1)               # 每一行的平均数，一行表示n_estimators的f1_score 
train_std1= train_scores1.std(axis=1)
test_means1 = test_score1.mean(axis=1)
test_std1 = test_score1.std(axis=1)

train_scores2, test_score2 = ms.validation_curve(model2, x, y, 'max_depth', max_depth, cv=5)
train_means2 = train_scores2.mean(axis=1)
train_std2= train_scores2.std(axis=1)
test_means2 = test_score2.mean(axis=1)
test_std2 = test_score2.std(axis=1)

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