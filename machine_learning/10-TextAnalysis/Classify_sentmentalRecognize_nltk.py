# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:52:01 2018

@author: Administrator
"""

'''
情绪分类：基于nltk库中朴素贝叶斯分类模型
ntlk模型的输入参数和格式  ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
'''

import nltk.corpus as nc                        # nltk语料库reader
import nltk.classify as cf
import nltk.classify.util as cu

pdata = []
fileids = nc.movie_reviews.fileids('pos')       # 正面评价文件名：pos
for fileid in fileids:
    feature = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        feature[word] = True                    # 出现的词全部都算 positive
    pdata.append((feature, 'POSITIVE'))
#print(pdata[:2])

ndata = []
fileids = nc.movie_reviews.fileids('neg')       # 正面评价文件名：pos
for fileid in fileids:
    feature = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        feature[word] = True                    # 出现的词全部都算negative
    ndata.append((feature, 'NEGATIVE'))

pnumb, nnumb = int(len(pdata)*0.8), int(len(ndata)*0.8)
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]

model = cf.NaiveBayesClassifier.train(train_data)
ac = cf.accuracy(model, test_data)              # cf / cu都可以
print(ac)                                       # 0.735

tops = model.most_informative_features()        # len:100  -- 最重要的特征(可用作筛选关键词)
print(tops[:10])                                # [('outstanding', True), ('insulting', True), ..

reviews = ['It is an amazing movie.', 
           'This is a dull movie, I would never recommend it to anyone', 
           'The cinematography is pretty great in this movie',
           'The directin was terrible and the story was all over the place',
           'I have no words to say']
sents, probs = [], []                           # 初始化类别和置信概率
for review in reviews:
    feature = {}
    words = review.split(' ')                   # 拆词：可用nltk的拆词器
    '''
    tokens = tk.word_tokenize(doc)              # nltk拆词器：按单词划分
    for i, token in enumerate(tokens):
        print(i+1, token)
    '''
    for word in words:
        feature[word] = True
    pred_class = model.prob_classify(feature)   # 同时获得类别和置信概率  参数，输入，输出？？？
    sent = pred_class.max()                     # 概率最大的类别
    prob = pred_class.prob(sent)                # 概率最大类别的概率  参数，输入，输出？？？
    sents.append(sent)
    probs.append(prob)
for review, sent, prob in zip(reviews, sents, probs):
    print(review, '->', sent, round(prob, 3))



'''
import nltk.corpus as nc
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus files in a variety of formats.  These
functions can be used to read both the corpus files that are
distributed in the NLTK corpus package, and corpus files that are part
of external corpora.
'''