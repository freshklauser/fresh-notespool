# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:11:48 2018

@author: Administrator
"""
'''
推荐引擎：基于Pearson Distance的电影推荐

欧几里得距离 Euclidean Distance： 需要自己计算
score = 1 / (1 + np.sqrt(((x - y) ** 2).sum()))    # 欧氏距离
缺点：计算的是绝对距离，没有考虑不同样本score的标准不同

Pearson Distance 皮氏距离：两个样本的协方差
score = np.corrcoef(x, y)[0,1]                      # 皮氏距离
'''

import json
import numpy as np

with open('ratings.json', 'r') as f:
    ratings = json.loads(f.read())          # dict
#{'John Carson': {'Inception': 2.5, 'Pulp Fiction': 3.5, 'Anger Management': 3.0, 'Fracture': 3.5, 'Serendipity': 2.5, 'Jerry Maguire': 3.0},
#'Michelle Peterson': {'Inception': 3.0, 'Pulp Fiction': 3.5, 'Anger Management': 1.5, 'Fracture': 5.0, 'Jerry Maguire': 3.0, 'Serendipity': 3.5}, ...

users = list(ratings.keys())                # 获取用户列表
# ['John Carson', 'Michelle Peterson', 'William Reynolds', 'Jillian Hobart', 'Melissa Jones', 'Alex Roberts', 'Michael Henry']

score_matrix = []                           # 初始化 得分矩阵
for user1 in users:                         # 遍历，计算每一个用户与其他用户的es / ps距离
    score_row = []
    for user2 in users:
        movies = set()                      # 空集合
        for movie in ratings[user1]:        # 基本dict取key用法 判断user1和user2的电影清单里是否有相同的movie
            if movie in ratings[user2]:
                movies.add(movie)           # 相同的电影添加到movies集合中
        if len(movies) == 0:                # 没有相同的movie
            score = 0
        else:
            x, y =[], []                    # 初始化 x:user1对movie的评分； y:user2对movie的评分
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
#            score = 1 / (1 + np.sqrt(((x - y) ** 2).sum()))    # 欧氏距离得分
            score = np.corrcoef(x, y)[0,1]                      # 皮氏距离得分 np.corrcoef(x, y)返回的是矩阵
        score_row.append(score)             # user1与所有users的相似度得分，占1行
    score_matrix.append(score_row)          # 行 --> matrix

users = np.array(users)                     # 转化为方便输入输出的数组格式
score_matrix = np.array(score_matrix)

for score_row in score_matrix:
    print(' '.join('{:5.2f}'.format(score) for score in score_row))
#users  1     2     3     4    5      6    7
#-------------------------------------------------
#  1  1.00  0.40  0.40  0.57  0.59  0.75  0.99
#  2  0.40  1.00  0.20  0.31  0.41  0.96  0.38
#  3  0.40  0.20  1.00  1.00 -0.26  0.13 -1.00
#  4  0.57  0.31  1.00  1.00  0.57  0.03  0.89
#  5  0.59  0.41 -0.26  0.57  1.00  0.21  0.92
#  6  0.75  0.96  0.13  0.03  0.21  1.00  0.66
#  7  0.99  0.38 -1.00  0.89  0.92  0.66  1.00

# 对A，与A相似的用户 按相似度得分高低排序
for i, user in enumerate(users):
    sorted_indices = score_matrix[i].argsort()[::-1]        # 获取间接排序的降序索引
    # [0 6 5 4 3 2 1]
    # [1 5 4 0 6 3 2] ...
    sorted_indices = sorted_indices[sorted_indices != 1]    # 过滤掉索引值==1的元素，即score==1,即user_i与其自身的相似度得分
    # [0 6 5 4 3 2 1]  ---> [0 6 5 4 3 2]
    # [1 5 4 0 6 3 2]  ---> [5 4 0 6 3 2] ...

    similar_users = users[sorted_indices]                   # 根据索引获得相似度值降序排列的相似用户列表
    similar_scores = score_matrix[i, sorted_indices]        # 根据索引获得相似度值降序排列的相似度矩阵的行列表

    positive_mask = similar_scores > 0                      # 过滤相似度值为负数的bool型掩码索引
    similar_users = similar_users[positive_mask]            # 过滤掉相似度值为负数的相似用户
    similar_scores = similar_scores[positive_mask]          # 过滤掉相似度值为负数的相似用户的相似度得分
#    print('similar_Users:', user, '->', similar_users, '\n', similar_scores, end='\n\n')

    '''
    推荐清单
    相似度作为权重，电影评分作为基础
    '''
    score_sums, weight_sums = {}, {}
    for similar_user, similar_score in zip(similar_users, similar_scores):
        for movie, score in ratings[similar_user].items():
            if movie not in ratings[user].keys():
                if movie not in score_sums.keys():
                    score_sums[movie] = 0
                score_sums[movie] += score * similar_score

                if movie not in weight_sums.keys():
                    weight_sums[movie] = 0
                weight_sums[movie] += similar_score
    '''
    推荐度：得分和相似度的加权平均 degree_recom = sum(score * similar_degreee) / sum(similar_degree)
    '''
    movie_ranks = {}
    for movie, score_sum in score_sums.items():
        movie_ranks[movie] = score_sum / weight_sums[movie]
    sorted_indices = np.array(list(movie_ranks.values())).argsort()[::-1]
    recomms = np.array(list(movie_ranks.keys()))[sorted_indices]
    print(user, '->', recomms)

#print('similar_Degree:', score_matrix[4])
#print('similar_Users:', users[4], '->', similar_users, '\n', similar_scores, end='\n\n')
#print('list_Recommend:', users[4], '->', recomms)


