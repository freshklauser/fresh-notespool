# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:11:48 2018

@author: Administrator
"""
'''
欧几里得距离 Euclidean Distance： 需要自己计算
缺点：计算的是绝对距离，没有考虑不同样本score的标准不同

Pearson Distance 皮氏距离：两个样本的协方差
score = np.corrcoef(x, y)[0,1]                      # 皮氏距离 
'''

import json
import numpy as np

with open('ratings.json', 'r') as f:
    ratings = json.loads(f.read())          # dict

users = list(ratings.keys())                # 获取用户列表
#print(ratings['Michelle Peterson'])
score_matrix = []                           # 初始化 得分矩阵
for user1 in users:                         # 遍历，计算每一个用户与其他用户的es距离
    score_row = []
    for user2 in users:
        movies = set()
        for movie in ratings[user1]:        # 基本dict取key用法 判断user1和user2的电影清单里是否有相同的movie
            if movie in ratings[user2]:
                movies.add(movie)           # 相同的电影添加到movies集合中
        if len(movies) == 0:
            score = 0
        else:
            x, y =[], []
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
#            score = 1 / (1 + np.sqrt(((x - y) ** 2).sum()))    # 欧氏距离
            score = np.corrcoef(x, y)[0,1]                      # 皮氏距离    np.corrcoef(x, y)返回的是矩阵
        score_row.append(score)
    score_matrix.append(score_row)
users = np.array(users)
score_matrix = np.array(score_matrix)
for score_row in score_matrix:
#    print(type(list(score_row)))
    print(' '.join('{:5.2f}'.format(score) for score in score_row))
#     1.00  0.29  0.47  0.39  0.41  0.34  0.35
#     0.29  1.00  0.34  0.28  0.28  0.67  0.26
#     0.47  0.34  1.00  0.54  0.39  0.32  0.39
#     0.39  0.28  0.54  1.00  0.31  0.32  0.36
#     0.41  0.28  0.39  0.31  1.00  0.29  0.40
#     0.34  0.67  0.32  0.32  0.29  1.00  0.27
#     0.35  0.26  0.39  0.36  0.40  0.27  1.00
    


'''
基本字典取key用法：
dict_s = {'Inception': 3.0, 'Pulp Fiction': 3.5, 'Anger Management': 1.5, 'Fracture': 5.0, 'Jerry Maguire': 3.0, 'Serendipity': 3.5}

for a in dict_s:
    print(a)
    
Inception
Pulp Fiction
Anger Management
Fracture
Jerry Maguire
Serendipity

基本tuple添加元素
movies = set()
movies.add('atasdf')


相关性矩阵：
corrcoef_ab = np.corrcoef(a,b)
[var(a)/std(a)std(a)=1  cov(a,b)/std(a)std(b)
 cov(b,a)/std(b)std(a)  var(b)/std(b)std(b)=1]
numpy.corrcoef(a,b) --> 相关性矩阵
相关性系数：
corrcoef_ab = np.corrcoef(a,b)[0,1]

'''