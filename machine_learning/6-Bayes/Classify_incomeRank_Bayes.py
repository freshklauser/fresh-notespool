# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:54:59 2018

@author: Administrator
"""
'''
朴素贝叶斯分类器：预测工资收入等级
'''

import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb

# 自定义编码器
class DigitEncoder():
    def fit_transform(self, y):
        return y.astype(int)
    
    def transform(self, y):
        return y.astype(int)
    
    def inverse_transform(self, y):
        return y.astype(str)

# 计数器<=50k,  计数器>50k, 数据数量
num_less, num_more, max_each = 0, 0, 7500
data = []
with open('adult.txt', 'r') as f:
    for line in f.readlines():
        line_data = line[:-1].split(', ')           # line是字符串，切掉每行最后的换行符
        if line_data[-1] == '<=50K' and num_less < max_each:
            data.append(line_data)
            num_less +=1 
        elif line_data[-1] == '>50K' and num_more < max_each:
            data.append(line_data)
            num_more += 1
        if num_less >= max_each and num_more >= max_each:
            break

data = np.array(data).T                 # 行优先，转置 方便处理特征的数据类型 # (15000, 15)
encoders, x = [], []
for row in range(len(data)):
#    print(data[2,0])
    if data[row, 0].isdigit():          # 数字，用自定义的encoder
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()     # 非数字，用sp的标签编码器
    if row < len(data) - 1:             # 前n-1行 x, 最后一行y
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T                       # 数据集还原

# 训练集和测试集划分
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.25, random_state=7)
# 朴素贝叶斯模型
model = nb.GaussianNB()

# 交叉验证评估模型性能
print(ms.cross_val_score(model, x, y, cv=10, scoring='f1_weighted').mean())     # 0.5867533673534193

# 训练模型
model.fit(train_x, train_y)
# 测试集预测
pred_test_y = model.predict(test_x)
# 查准率
print((pred_test_y == test_y).sum() / pred_test_y.size)                        # 0.6242666666666666

# 待预输入测数据
data = [['39','State-gov', '77516', 'Bachelors', '13', 'Never-married', 'Adm-clerical', 
         'Not-in-family','White', 'Male', '2174', '0', '40', 'United-States']]
# 待预测输入数据预处理
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
# 根据待预测输入数据 预测
pred_y = model.predict(x)
output_y = encoders[-1].inverse_transform(pred_y)                              # ['<=50K']
print(output_y)