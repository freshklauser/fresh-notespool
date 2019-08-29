# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:51:04 2018

@author: Administrator
"""

import nltk.stem as ns

words = ['table', 'probably', 'wolves', 'dreamt', 'palying', 'is', 'beaches', 'envision', 'grounded']
'''
词型还原
'''
lmm = ns.WordNetLemmatizer()

for word in words:
    n = lmm.lemmatize(word, pos='n')                    # pos='n' 按名次处理
    v = lmm.lemmatize(word, pos='v')                    # pos='v' 按动词处理
    print('{:10} {:10} {:10}'.format(word, n, v))
    #table      table      table     
    #probably   probably   probably  
    #wolves     wolf       wolves    
    #dreamt     dreamt     dream     
    #palying    palying    palying   
    #is         is         be        
    #beaches    beach      beach     
    #envision   envision   envision  
    #grounded   grounded   ground   