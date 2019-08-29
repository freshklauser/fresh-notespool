# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:51:04 2018

@author: Administrator
"""

import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

words = ['table', 'probably', 'wolves', 'dreamt', 'palying', 'is', 'beaches', 'envision', 'grounded']
'''
提取词干
'''
stemmer_porter = pt.PorterStemmer()                     # 偏宽松
stemmer_lancaster = lc.LancasterStemmer()               # 偏严格
stemmer_snowball = sb.SnowballStemmer('english')        # 适中
for word in words:
    pstem = stemmer_porter.stem(word)
    lstem = stemmer_lancaster.stem(word)
    sstem = stemmer_snowball.stem(word)
    print('{:10} {:10} {:10} {:10}'.format(word, pstem, lstem, sstem))
    #table      tabl       tabl       tabl      
    #probably   probabl    prob       probabl   
    #wolves     wolv       wolv       wolv      
    #dreamt     dreamt     dreamt     dreamt    
    #palying    pali       paly       pali      
    #is         is         is         is        
    #beaches    beach      beach      beach     
    #envision   envis      envid      envis     
    #grounded   ground     ground     ground    