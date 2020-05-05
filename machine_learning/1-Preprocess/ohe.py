# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:18:14 2018

@author: Administrator
"""

import numpy as np
import sklearn.preprocessing as sp

raw_samples2 = np.array([
    [1, 3, 2],
    [7, 5, 4],
    [1, 8, 6],
    [7, 3, 9]])
print(raw_samples2, '\n')
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
# [[1 0 1 0 0 1 0 0 0]
# [0 1 0 1 0 0 1 0 0]
# [1 0 0 0 1 0 0 1 0]
# [0 1 1 0 0 0 0 0 1]]
# 调用ohe的fit_transform方法进行样本独热编码
new_sample = np.array([1, 5, 6])
ohe_sample = ohe.transform([new_sample])       # 沿用已有的编码表时用transform，原始表中没有的值会拒绝编码
print(ohe_sample)  # [[1 0 0 1 0 0 0 1 0]]


# 独热编码的code原理实现:
code_tables = []
for col in raw_samples2.T:
    code_table = {}
    # dict-key:每个元素作为dict的key
    for val in col:
        code_table[val] = None
    code_tables.append(code_table)
#    print(code_table.keys())    # dict_keys([1, 7]), dict_keys([3, 5, 8]), dict_keys([2, 4, 6, 9])
# print(code_tables)
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
print(ohe_samples)
#[[1 0 1 0 0 1 0 0 0]
# [0 1 0 1 0 0 1 0 0]
# [1 0 0 0 1 0 0 1 0]
# [0 1 1 0 0 0 0 0 1]]
