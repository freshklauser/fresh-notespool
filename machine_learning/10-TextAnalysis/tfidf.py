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

'''
1）文档     --> 词袋矩阵
2）词袋矩阵 --> TF-IDF
'''
cv = ft.CountVectorizer()                       # 矢量化器
bow = cv.fit_transform(sentences).toarray()     # 词袋矩阵 不加.toarray() 稀疏矩阵
#[[0 1 1 0 0 1 0 1 1]
# [2 0 1 0 1 1 1 0 2]
# [0 0 0 1 1 1 1 1 1]]

words = cv.get_feature_names()                  # 获取词袋矩阵对应的特征名称
print(words)
#['black', 'brown', 'dog', 'forbidden', 'in', 'is', 'room', 'running', 'the']

term_frequency = sp.normalize(bow, norm='l1')  # 词频矩阵---词袋矩阵归一化处理
print(term_frequency)

# TF-IDF: 词袋矩阵--> 数字化特征
term_tt = ft.TfidfTransformer()                 # 词频逆文档频率转换器
tfidf = term_tt.fit_transform(bow).toarray()    # 不toarray的话是稀疏矩阵，更省内存
print(tfidf)
#[[0.         0.59188659 0.45014501 0.         0.         0.34957775  0.         0.45014501 0.34957775]
# [0.73130492 0.         0.27808812 0.         0.27808812 0.21596023  0.27808812 0.         0.43192047]
# [0.         0.         0.         0.53972482 0.41047463 0.31877017  0.41047463 0.41047463 0.31877017]]


'''
矢量化器：
class CountVectorizer(BaseEstimator, VectorizerMixin):
    """Convert a collection of text documents to a matrix of token counts(出现次数)
'''