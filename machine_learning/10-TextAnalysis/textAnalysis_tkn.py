# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:51:04 2018

@author: Administrator
"""

import nltk.tokenize as tk
doc = "Are you curious about tokenization？Let's see how it woeks!"\
      "we need to analyse a couple of sentences" \
      "with punctuations to see it in action."
#print(doc)

'''
分词
'''
tokens = tk.sent_tokenize(doc)              # 拆句子：按句子划分
for i, token in enumerate(tokens):
    print(i+1, token)
    
tokens = tk.word_tokenize(doc)              # 拆词：按单词划分
print('tokens',tokens)
for i, token in enumerate(tokens):
    print(i+1, token)
    
tokenizer = tk.WordPunctTokenizer()         # 拆词：
tokens = tokenizer.tokenize(doc)
for i, token in enumerate(tokens):
    print(i+1, token)
