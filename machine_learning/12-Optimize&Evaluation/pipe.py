# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 10:04:14 2018

@author: Administrator
"""

import numpy as np
import sklearn.datasets as sd
import sklearn.feature_selection as fs
import sklearn.ensemble as se
import sklearn.pipeline as spp
import sklearn.model_selection as ms
import matplotlib.pyplot as plt

'''
样本生成器：
n_samples:样本个数
n_features :特征个数= n_informative（） + n_redundant + n_repeated
n_informative：多信息特征的个数
n_redundant：冗余信息，informative特征的随机线性组合
n_repeated ：重复信息，随机提取n_informative和n_redundant 特征
n_classes：分类类别
n_clusters_per_class ：某一个类别是由几个cluster构成的
random_state：随机种子，使得实验可重复
n_classes*n_clusters_per_class 小于或等于 2^n_informative
'''
x, y = sd.samples_generator.make_classification(n_samples=200,          # 样本总个数
                                                n_informative=4,        # 多信息特征
                                                n_features=20,          # 20个特征
                                                n_redundant=0,          # 冗余特征个数
                                                random_state=5
                                                )


'''
特征选择器： 优选出k个特征作为主要特征
 |  Parameters
 |  ----------
 |  score_func : callable
 |      Function taking two arrays X and y, and returning a pair of arrays
 |      (scores, pvalues) or a single array with scores.
 |      Default is f_classif (see below "See also"). The default function only
 |      works with classification tasks.
 |  k : int or "all", optional, default=10
 |      Number of top features to select.
 |      The "all" option bypasses selection, for use in a parameter search.
'''
skb = fs.SelectKBest(fs.f_regression,                                   # 回归规则作为特征个数选择的规则
                     k=5,                                               # 选出k个主要特征
                     )


# 随机森林分类器
rfc = se.RandomForestClassifier(n_estimators=25,                        # 决策树个数
                                max_depth=4,                            # 树高最大4
                                random_state=7                          # 随机种子源
                                )

# 构建管线： 区别make_pipeline用法，make_pipeline不能给管线自定义命名
model = spp.Pipeline([('selector', skb),                                #  顺序：输入skb， skb管线的输出作为rfc的输入
                      ('classifier', rfc)])

# 模型性能评估：f1_score
print('f1_score_0:', ms.cross_val_score(model, x, y, cv=10, scoring='f1_weighted').mean()) # 0.7631188256188256

# 参数修改:selector为Pipeline参数中自定义的名字selector, 后面加2个_
model.set_params(selector__k=2,
                 classifier__n_estimators=10
                 )

# 修改参数后评估模型性能
print('f1_score_r:', ms.cross_val_score(model, x, y, cv=10, scoring='f1_weighted').mean()) # 0.6943056943056943
# 训练修改参数后的优选模型
model.fit(x, y)

# 优选模型实际分类用到的有效特征 (n_features中selected_mask==True的特征)
selected_mask = model.named_steps['selector'].get_support()             # (20,)
print('selected_mask:',selected_mask)                                   # [...False True False False...]

# 筛选出实际分类用到的有效特征：选择基于掩码为真的数组索引
selected_indices_tuple = np.where(selected_mask==True)                  # tuple: (array([ 9, 15], dtype=int64),),见np.where()的用法
selected_indices = selected_indices_tuple[0]                            # array: array([ 9, 15]
print('selected_indices:', selected_indices)                            # selected_indices: [ 9 15]



# 根据优选的有效特征重新定义数据集x: 只含有selected_indices.shape[0]个特征的样本数据
x = x[:, selected_indices]              # 只有2个特征时才能画散点图，多个点无法画图
# 根据新的数据集训练模型
model.fit(x, y)




l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005

grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v)) # 栅格点阵
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]         # 栅格横坐标拉平成1维，预测一维栅格分类值
flat_y = model.predict(flat_x)                               # 一维栅格分类值(作为颜色区分pcolormesh的c)
grid_y = flat_y.reshape(grid_x[0].shape)                     # 栅格分类reshape与grid_x一样

plt.figure('Selector_Classfier Pipeline', facecolor='lightgray')
plt.title('Selector_Classfier Pipeline', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='Dark2')
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='cool', s=30)

plt.show()

'''
获取array数组的下标：`np.where()[0]` 
通过下标数组返回数组中的元素集：`np.take()`
注：`np.where()`的return: `tuple((arr_indices, arr_dtype), )`
'''
