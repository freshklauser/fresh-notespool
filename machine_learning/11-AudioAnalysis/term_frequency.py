# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:16:22 2018

@author: Administrator
"""

import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft        # 特征抽取模块
import sklearn.preprocessing as sp

doc = 'The brown dog is running. The black dog is in the black room. Running in the room is forbidden.'
print(doc)

sentences = tk.sent_tokenize(doc)
for i, sentence in enumerate(sentences):
    print(i+1, sentence)

cv = ft.CountVectorizer()                       # 矢量化器
'''
class CountVectorizer(BaseEstimator, VectorizerMixin):
    """Convert a collection of text documents to a matrix of token counts(出现次数)
'''
bow = cv.fit_transform(sentences).toarray()     # 词袋矩阵
#[[0 1 1 0 0 1 0 1 1]
# [2 0 1 0 1 1 1 0 2]
# [0 0 0 1 1 1 1 1 1]]

words = cv.get_feature_names()                  # 获取词袋矩阵对应的特征名称
print(words)
#['black', 'brown', 'dog', 'forbidden', 'in', 'is', 'room', 'running', 'the']

term_frequency = sp.normalize(bow, norm='l1')   # 词频矩阵---词袋矩阵归一化处理
print(term_frequency)