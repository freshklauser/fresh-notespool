# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:16:22 2018

@author: Administrator
"""
'''
文档分类：TF-IDF , 基于多项式分布的朴素贝叶斯模型
TF-IDF（term frequency–inverse document frequency）:词频-逆文本频率
'''

import numpy as np
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft  # 文本特征提取模块
import sklearn.naive_bayes as nb              # 朴素贝叶斯分类器

train = sd.load_files('../ML/data/20news', 
                      encoding='latin1', 
                      shuffle=True,             # 打乱数据顺序
                      random_state=7
                      )
train_data = train.data                         # len(train_data) : 2968
#print(train_data[:10])

train_y = train.target
print(train_y[:10])                        # [4 4 0 2 2 1 0 4 4 1]   set(train_y):{0, 1, 2, 3, 4}

categories = train.target_names            # list： categories
print(categories)                          # ['misc.forsale', 'rec.motorcycles', 'rec.sport.baseball', 'sci.crypt', 'sci.space']
categories = np.array(categories)          # list --> array
print(categories[train_y])                 # 序号对应特征名称： 分类序号train_y <--> 特征名称categories
print('train_y==1:',categories[1])         # train_y==1: rec.motorcycles

# 文本 --> 词袋矩阵train_bow
cv = ft.CountVectorizer()                  # 矢量化器 Convert a collection of text documents to a matrix of token counts
train_bow = cv.fit_transform(train_data)   # (2968, 40605)
# 词袋矩阵train_bow --> TF-IDF train_x
term_tt = ft.TfidfTransformer()            # TF-IDF转换器
train_x = term_tt.fit_transform(train_bow) # 利用TF-IDF转换器： 词袋矩阵 --> TF-IDF

# naive_bayes模型训练
# GaussianNB：基于高斯正态分布计算密度函数
# MultinomialNB ：基于多项式分布计算密度函数
model = nb.MultinomialNB()              # 多项分布的朴素贝叶斯模型， 文本在文档中的分布？？？
model.fit(train_x, train_y)


# 测试模型
test_data = ['The curveballs of right handed pitches tend to curve to the curve',
             'Caesar cipher is an ancient form of encryption',
             'This two-wheeler is really good on slippery roads']

test_bow = cv.transform(test_data)      # 文本 --> 词袋矩阵
test_x = term_tt.transform(test_bow)    # 利用TF-IDF转换器：词袋矩阵 --> TF-IDF
pred_test_y = model.predict(test_x)     # 模型预测
print(pred_test_y)                      # [2 3 1]
output_y = categories[pred_test_y]      # TF-IDF预测结果 --> 文本
print(output_y)                         # ['rec.sport.baseball' 'sci.crypt' 'rec.motorcycles']

'''
矢量化器：
class CountVectorizer(BaseEstimator, VectorizerMixin):
    """Convert a collection of text documents to a matrix of token counts(出现次数)
'''