# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:32:28 2018

@author: Administrator
"""
'''
主题词提取:隐含狄利克雷分布(LDA(Latent Dirichlet allocation))应用           ??????????
'''

import warnings
warnings.filterwarnings('ignore', category=UserWarning)
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm                    # 隐含狄利克雷分布模型 LDA(线性判别分析)
import gensim.corpora as gc

doc = []
with open('topic.txt', 'r') as f:
    for line in f.readlines():
        doc.append(line[:-1])
tokenizer = tk.RegexpTokenizer(r'\w+')                # reg 匹配特殊的分隔符
stopwords = nc.stopwords.words('english')             # 停止词，没实际语义贡献的词
stemmer = sb.SnowballStemmer('english')
lines_tokens = []
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)

#Dictionary： encapsulates(封装) the mapping between normalized words and their integer ids.
dic = gc.Dictionary(lines_tokens)
# Dictionary(121 unique tokens: ['cryptographi', 'lot', 'spent', 'studi', 'time']...)
bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)              # 文档 --> 词袋
    bow.append(row)
#print(bow)

n_topic = 2                                     # 指定聚类类别个数
model = gm.LdaModel(bow,                        # 词袋模型
                    num_topics=n_topic,         # 类别数目参数
                    id2word=dic
                    )
topics = model.print_topics(num_topics=n_topic,
                            num_words=4,        # 每个主题词的字数
                            )                   # 打印主题, 字符串
print(topics)
#[(0, '0.026*"spaghetti" + 0.018*"need" + 0.017*"made" + 0.016*"modern"'), 
# (1, '0.034*"spaghetti" + 0.019*"italian" + 0.019*"cryptographi" + 0.017*"use"')]