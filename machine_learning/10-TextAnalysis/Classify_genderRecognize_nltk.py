# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 11:13:49 2018

@author: Administrator
"""
'''
性别识别：基于nltk库中朴素贝叶斯分类模型
ntlk模型的输入参数和格式  ？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？
'''

import random
import numpy as np
import nltk.corpus as nc                     # nltk语料库reader
import nltk.classify as cf                   # 自然语言包的分类器,效率没有sklearn中的分类器效率高

male_names = nc.names.words('male.txt')
female_names = nc.names.words('female.txt')
#print(len(male_names))

models, acs = [], []                        # 模型，精度得分
for n_letters in range(1, 6):               # 取名字最后n_letters个字母
    data = []                               # 输入数据不同于sklearn, 不是一行一样本 一列一特征
    for male_name in male_names:
        # 输入：特征向量格式 dict表示
        feature = {'feature':male_name[-n_letters:].lower()}  # nltk特征值格式要求。截取名字最后n_letters个字母，转换为小写，作为特征值
        data.append((feature, 'male'))      # nltk自动进行数字化处理，不需要额外处理
    for female_name in female_names:
        # 输入：特征向量格式 dict表示，
        feature = {'feature':female_name[-n_letters:].lower()}
        data.append((feature, 'female'))
    
    random.seed(7)
    random.shuffle(data)                    # 打乱数据顺序
    
    train_data = data[:int(len(data)/2)]    # 划分训练集和测试集
    test_data = data[int(len(data)/2):]
    
    # nltk模型训练中train_data不用区分x,y
    model = cf.NaiveBayesClassifier.train(train_data)       # nltk包的朴素贝叶斯分类器,.train(train_data)方法直接训练数据
    ac = cf.accuracy(model, test_data)                      # 精度，模型评估
    
    models.append(model)
    acs.append(ac)

best_index = np.array(acs).argmax()
best_letters = best_index + 1
best_model = models[best_index]
best_ac = acs[best_index]
print(best_letters, best_ac)                                # 2 0.7781973816717019
names = ['Leonardo', 'Amy', 'Sam', 'Tom', 'Katherine', 'Taylor', 'Susanne']
genders = []
for name in names:
    feature= {'feature': name[-best_letters:].lower()}
    gender = best_model.classify(feature)                   # 值获得分类，不获得置信概率
    genders.append(gender)

for name, gender in zip(names, genders):
    print(name, '->', gender)
#    Leonardo -> male
#    Amy -> female
#    Sam -> male
#    Tom -> male
#    Katherine -> female
#    Taylor -> male
#    Susanne -> female
    
    