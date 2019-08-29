# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:17:32 2018

@author: Administrator
"""

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

import numpy as np
import sklearn.preprocessing as sp

# 数据源
raw_samples = np.array(['audi', 'ford', 'ford', 'bmw', 'toyota', 'ford', 'audi'])
print(raw_samples)

lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)        # 排序后编码
print(lbe_samples)                      # [0 2 2 1 3 2 0]

raw_samples = lbe.inverse_transform(lbe_samples)
print(raw_samples)