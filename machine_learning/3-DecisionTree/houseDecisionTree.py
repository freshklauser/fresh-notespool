# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:05:47 2018

@author: Administrator
"""

'''
原理：
A.自助聚合-- Bagging（套袋法）
    采用有放回的抽样规则，从m个样本中随机抽取n个样本，构建一棵决策树，重复以上过程b次，
得到b棵决策树。利用每棵决策树的预测结果，根据平均或者投票得到最终预测结果。

B.随机森林(使用较多)：行和列的挑选都是局部化 --  Bagging（套袋法）
    在自助聚合算法的基础上更进一步，对特征也应用自助聚合，即每次训练时，不是用所有的
特征构建树结构，而是随机选择部分特征参与构建，以此避免特殊特征对预测结果的影响。

C.正向激励（不断调整样本权重）-- Boosting（提升法）
    初始化时，针对m个样本分配初始权重，然后根据这个带有权重的模型预测训练样本，针对
那些预测错误的样本，提高其权重，再构建一棵决策树模型，重复以上过程，得到b棵决策树。
评估器数：b

决策树：
sklearn.tree.DecisionTreeRegressor()
    --> 决策树回归器

正向激励：
sklearn.ensemble.AdaBoostRegressor(元回归器，
                                   n_estimators=评估器数 --b，
                                   random_state=随机种子源  一般选5或7)
    --> 正向激励回归器
random_state:此参数让结果容易复现。 一个确定的随机值将会产生相同的结果，在参数和训练数据不变的情况下.
    
随机森林：
sklearn.ensemble.RandomForestRegressor(max_depth=最大树高,
                                       n_estimators=评估器数 --b,
                                       min_samplses_split=划分子表的最小样本数)
min_samples_split: 内部节点再划分所需最小样本数，默认2。这个值限制了子树继续划分的条
件，如果某节点的样本数少于min_samples_split，则不会继续再尝试选择最优特征来进行划分。 
默认是2.如果样本量不大，不需要管这个值。如果样本量数量级非常大，则推荐增大这个值。


    --> 随机森林回归器
代码：
决策树模型.feature_importances_ ： 特征重要性(根据训练过程中信息熵的计算得到的)
代码：feature_import.py
'''

import sklearn.datasets as sd           # 数据包
import sklearn.utils as su              # 小工具包
import sklearn.tree as st
import sklearn.ensemble as se           # 机器学习集成方法模块 
import sklearn.metrics as sm            # 评估模型效果

# 获取标准数据集
housing = sd.load_boston()              # 自带数据集,<class 'sklearn.utils.Bunch'>
print(housing.feature_names)            # 特征名称
#['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
print(housing.data.shape)               # (506, 13)
print(housing.target.shape)             # 目标：预测的房价

# trainning_set, testing_set
x, y = su.shuffle(housing.data, housing.target,random_state=7)      # 打乱数据顺序，形成无序数据集
train_size = int(len(x) * 0.8)                                      # 数据集的80%作为训练集, 20%作为测试集
train_x, test_x, train_y, test_y = x[:train_size], x[train_size:], y[:train_size], y[train_size:]


# 决策树模型
model = st.DecisionTreeRegressor(max_depth=5)       # 最大树高4层
model.fit(train_x, train_y)                         # 
pred_test_y = model.predict(test_x)                 # 模型预测值 若==test_y，则完全吻合
print(sm.r2_score(test_y, pred_test_y))             # 0.8450752976507327


# 基于决策树的正向激励模型 （元回归器 == 决策树回归器）
model = se.AdaBoostRegressor(st.DecisionTreeRegressor(max_depth=5),     # 元回归器：决策树回归器
                             n_estimators=500,                          # 评估器数b 即决策树的个数
                             random_state=7                             # 随机种子源 一般选5或7
                             )
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print('AB:', sm.r2_score(test_y, pred_test_y))             # 0.9148573795541087

for test, pred_test in zip(test_y, pred_test_y):
    print(test, '-->', pred_test)
#    14.9 --> 15.125000000000002
#    21.7 --> 20.932142857142857
#    24.4 --> 26.11458333333334
#    ...
    

'''
集成学习方法模块sklearn.ensemble：
dir(sklearn.ensemble)
Out[169]: 
['AdaBoostClassifier',
 'AdaBoostRegressor',
 'BaggingClassifier',
 'BaggingRegressor',
 'BaseEnsemble',
 'ExtraTreesClassifier',
 'ExtraTreesRegressor',
 'GradientBoostingClassifier',
 'GradientBoostingRegressor',
 'IsolationForest',
 'RandomForestClassifier',
 'RandomForestRegressor',
 'RandomTreesEmbedding',
 'VotingClassifier',
 '__all__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__path__',
 '__spec__',
 '_gradient_boosting',
 'bagging',
 'base',
 'forest',
 'gradient_boosting',
 'iforest',
 'partial_dependence',
 'voting_classifier',
 'weight_boosting']
'''