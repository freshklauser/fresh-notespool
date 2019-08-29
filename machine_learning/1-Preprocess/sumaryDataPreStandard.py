# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 19:30:16 2018

@author: Administrator
"""
'''
数据预处理：

'''

import numpy as np
import sklearn.preprocessing as sp
import matplotlib.pyplot as plt

# 数据源1
raw_samples = np.array([
        [3, -1.5, 2, -5.4],
        [0, 4, -0.3, 2.1],
        [1, 3.3, -1.9, -4.3]])
# 数据源2
raw_samples2 = np.array([
        [1, 3, 2],
        [7, 5, 4],
        [1, 8, 6],
        [7, 3, 9]])
# 数据源3
raw_samples3 = np.array(['audi', 'ford', 'ford', 'bmw', 'toyota', 'ford', 'audi'])



'''
1）均值移除：为了统一样本矩阵中不同特恒的基准值和分散度，可以将各个特征的
         平均值调整为0，标准差调整为1，这个过程称为均值移除。
sklearn.preprocessing.scale(原始样本矩阵) 
    --> return：均值移除后的样本矩阵(mean=0, std=1)
def scale(X, axis=0, with_mean=True, with_std=True, copy=True):
    Standardize a dataset along any axis
'''
samples = sp.scale(raw_samples) # 标准化样本均值和标准差(mean=0, std=1)
print('samples:', samples)
print(samples.mean(axis=0))     # [ 5.55111512e-17 -1.11022302e-16 -7.40148683e-17 -7.40148683e-17]
print(samples.std(axis=0))      # [1. 1. 1. 1.]



'''
2）范围缩放：统一样本矩阵中不同特征的最大值和最小值范围
sklearn.preprocessing.MinMaxScaler(feature_range=期望最小最大值, copy=True)
    --> return: 范围缩放器
                范围缩放器.fit_transform(原始样本矩阵)
                    --> return：范围缩放后的样本矩阵
    Parameters
    ----------
    feature_range : tuple (min, max), default=(0, 1)
        Desired range of transformed data.
    copy : boolean, optional, default True
        Set to False to perform inplace row normalization and avoid a
        copy (if the input is already a numpy array).
'''
mms = sp.MinMaxScaler(feature_range=(0, 1))         # 样本标准化到(0,1)之间
mms_samples = mms.fit_transform(raw_samples)        # 缩放后的样本矩阵
print(mms_samples)                                  # range(0,1)
#[[1.         0.         1.         0.        ]
# [0.         1.         0.41025641 1.        ]
# [0.33333333 0.87272727 0.         0.14666667]]


'''
3）归一化：为了用占比表示特征，用每个样本的特征值除以该样本的特征值绝对值之和，以
        使每个样本的特征值绝对值之和为1。 （转化为占比 normalized）
sklearn.preprocessing.normalize(原始样本矩阵，norm='l1')
	--> return：归一化后的样本矩阵
l1即L1范数，矢量中各元素绝对值之和。
l2即L2范数，矢量元素绝对值的平方和再开方
def normalize(X, norm='l2', axis=1, copy=True, return_norm=False):
    norm : 'l1', 'l2', or 'max', optional ('l2' by default)
    The norm to use to normalize each non zero sample (or each non-zero feature if axis is 0).
'''
nor_samples = sp.normalize(raw_samples, norm='l1')  # 归一化：百分比
print(nor_samples)
#[[ 0.25210084 -0.12605042  0.16806723 -0.45378151]
# [ 0.          0.625      -0.046875    0.328125  ]
# [ 0.0952381   0.31428571 -0.18095238 -0.40952381]]



'''
4）二值化：用0和1来表示样本矩阵中相对于某个给定阈值高于或低于它的元素
sklearn.preprocessing.Binarizer(threshold=阈值, copy=True)        # copy default True
    --> return：二值化器
                二值化器.transform(原始样本矩阵) 
                    --> return: 二值化后的样本矩阵 （不可逆过程）--考虑独热编码
threshold: feature <= threshold: feature = 0;
                    > threshold: feature = 1.
'''
bins = sp.Binarizer(threshold=1.4)              # 构建二值化器
bins_samples = bins.transform(raw_samples)      # 样本二值转换， 不可逆
print(bins_samples)
#[[1. 0. 1. 0.]
# [0. 1. 0. 1.]
# [0. 1. 0. 0.]]



'''
5）独热编码     (稀疏矩阵)    什么情况下使用？？
sklearn.preprocessing.OneHoteEncoder(sparse=是否采用压缩格式, dtype=元素类型)
    --> return：独热编码器
                独热编码器.fit_transform(原始样本矩阵)
                --> return：独热编码后的样本矩阵，同时构建编码表字典
                独热编码器.transform(原始样本矩阵)
                 --> return：独热编码后的样本矩阵，使用已有的编码表字典
'''
# 生成独热编码器ohe
ohe = sp.OneHotEncoder(sparse=False, dtype=int)     # sparse default=True
# 调用ohe的fit_transform方法进行样本独热编码
ohe_samples = ohe.fit_transform(raw_samples2)
print(ohe_samples)
#[[1 0 1 0 0 1 0 0 0]
# [0 1 0 1 0 0 1 0 0]
# [1 0 0 0 1 0 0 1 0]
# [0 1 1 0 0 0 0 0 1]]
# 调用ohe的fit_transform方法进行样本独热编码
new_sample = np.array([1, 5, 6])
ohe_sample = ohe.transform([new_sample])       # 沿用已有的编码表时用transform，原始表中没有的值会拒绝编码
#print(ohe_sample)       #  [[1 0 0 1 0 0 0 1 0]]



'''
6）标签编码
不同Series即不同特征的编码表相互独立，编码和解码都要对应使用
将字符形式的特征值映射为整数
sklearn.preprocessing.LabelEncoder()
    --> return：标签编码器
                标签编码器.fit_transform(原始样本矩阵)
                    --> return：编码样本矩阵，构建编码字典
                标签编码器.transform(原始样本矩阵)
                    --> return：编码样本矩阵，使用已有编码字典
                标签编码器.inverse_transform(编码样本矩阵)
                    --> return：原始样本矩阵，使用编码字典
'''
# 生成标签编码器
lbe = sp.LabelEncoder()
# 标签编码
lbe_samples = lbe.fit_transform(raw_samples3)
print(lbe_samples)      # [0 2 2 1 3 2 0]   编码：基本排序后按序号编码
raw_samples_1 = lbe.inverse_transform(lbe_samples)      # 解码成str
#print(raw_samples_1)    # ['audi' 'ford' 'ford' 'bmw' 'toyota' 'ford' 'audi']




'''
独热编码原理code：
'''
# 独热编码的code原理实现:
code_tables = []
for col in raw_samples2.T:
    code_table = {}
    # dict-key:每个元素作为dict的key
    for val in col:
        code_table[val] = None
    code_tables.append(code_table)
#    print(code_table.keys())    # dict_keys([1, 7]), dict_keys([3, 5, 8]), dict_keys([2, 4, 6, 9])
#print(code_tables)  
# [{1: None, 7: None}, {3: None, 5: None, 8: None}, {2: None, 4: None, 6: None, 9: None}]

for code_table in code_tables:
    # 编码的个数
    size = len(code_table)
    for one, key in enumerate(sorted(code_table.keys())):   # 遍历有序键
#        print(key,one, sep='|')
        code_table[key] = np.zeros(shape=size, dtype=int)   # 每取出1个key,为其创建1个shape=size的零数组
#        print('code_table[key]:',code_table[key])
        code_table[key][one] = 1                            # 取出的顺序作为零数组的下标，对应赋值为1
#        print('code_table[key]:',code_table[key])           # [1,7] --> (i=0,key=1) (i=1,key=7)
                                                            # [0,0] --> [1,0]        [0,1]
#        code_table[key]: [1 0]
#        code_table[key]: [0 1]
#        code_table[key]: [1 0 0]
#        code_table[key]: [0 1 0]
#        code_table[key]: [0 0 1]
#        code_table[key]: [1 0 0 0]
#        code_table[key]: [0 1 0 0]
#        code_table[key]: [0 0 1 0]
#        code_table[key]: [0 0 0 1]
                                                            
ohe_samples = []
for raw_sample in raw_samples2:
#    print(raw_sample)
    ohe_sample = np.array([], dtype=int)
    # 编码并存入ohe_sample
    for i, key in enumerate(raw_sample):
        ohe_sample = np.hstack((ohe_sample, code_tables[i][key]))   # 行内依次取出水平拼接
    # 沿行方向即raw_sample如[1 3 2]编码完成后将行完整编码添加到ohe_samples列表中
    ohe_samples.append(ohe_sample)
ohe_samples = np.array(ohe_samples)
#print(ohe_samples)
#[[1 0 1 0 0 1 0 0 0]
# [0 1 0 1 0 0 1 0 0]
# [1 0 0 0 1 0 0 1 0]
# [0 1 1 0 0 0 0 0 1]]

















