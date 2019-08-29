# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 11:44:06 2018

@author: Administrator
"""
'''
参数优化的KMeans聚类模型
'''
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import sklearn.cluster as sc
import matplotlib.pyplot as plt

x = []
with open('perf.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line.split(',')]
        x.append(data)
x = np.array(x)                                              # (250, 2)

# 参数训练 选择最优的模型和聚类数
clusters, scores, models = np.arange(2, 11),[], []           # clusters:聚类数范围， 得分列表，模型列表
for n_cluster in clusters:
    # 模型构建： K均值聚类
    model = sc.KMeans(init='k-means++',                      # 初始化聚类中心
                      n_clusters=n_cluster,                  # 聚类数： n_clusters迭代
                      random_state=7                         # 随机种子，保证随机采样的可重现性
                      )
    # 训练模型
    model.fit(x)
    # 计算模型的轮廓系数
    score = sm.silhouette_score(x,                           # X：二维样本，通常为[n_samples, n_features]，当 metric 设置为”precomputed”时，应为[n_samples, n_samples]方阵
                                model.labels_,               # 样本所属的聚类类别，
                                sample_size=len(x),          # 样本大小
                                metric='euclidean'           # 欧几里得距离
                                )
    scores.append(score)
    models.append(model)
scores = np.array(scores)

best_index = scores.argmax()                                # 得分最高的索引
best_cluster = clusters[best_index]
print('best_cluster:', best_cluster)
best_score = scores[best_index]
print('best_score:', best_score)


# 未经参数训练的KMeans聚类模型
model = sc.KMeans(init='k-means++',                         # 初始化聚类中心
                  n_clusters=4)                             # 聚类数
model.fit(x)
centers = model.cluster_centers_


# 参数训练后的KMeans聚类模型
best_model = models[best_index]
best_centers = best_model.cluster_centers_
pred_y = best_model.predict(x)

# model.labels_
print(x[:5, :])                                             # 样本
print(best_model.labels_[:5])                               # 样本标签，即聚类类别 [0 2 1 4 3]
#     样本点           样本标签 model.labels_ 即聚类类别
#[[ 1.65  1.91]  ---->  0类
# [ 2.77  4.98]  ---->  2类
# [ 5.82  2.56]  ---->  1类
# [ 7.24  5.24]  ---->  4类
# [-0.3   4.06]] ---->  3类
print(best_centers)                                         # 将labels在centers点上备注出来 ？？？？？？？？？？？


'''
绘图:未经参数训练的KMeans聚类模型
'''
plt.figure('KMeansCluster', facecolor='lightgray', figsize=(7,9))

plt.subplot(211)
plt.title('K-KMeansCluster_unTrained', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005

grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v)) # 栅格点阵
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]         # 栅格横坐标拉平成1维，预测一维栅格分类值
flat_y = model.predict(flat_x)                               # 一维栅格分类值(作为颜色区分pcolormesh的c)
grid_y = flat_y.reshape(grid_x[0].shape)                     # 栅格分类reshape与grid_x一样
plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='binary')

plt.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=30)
plt.scatter(centers[:, 0], centers[:, 1], marker='+', c='gold', s=40)

'''
绘图:参数训练后的KMeans聚类模型
'''
plt.subplot(212)
plt.title('K-KMeansCluster_Trained', fontsize=14)
plt.xlabel('x_', fontsize=14)
plt.ylabel('y_', fontsize=14)
plt.tick_params(labelsize=10)

flat_y = best_model.predict(flat_x)                               # 一维栅格分类值(作为颜色区分pcolormesh的c)
grid_y = flat_y.reshape(grid_x[0].shape)                          # 栅格分类reshape与grid_x一样
plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='binary')

plt.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=30)
plt.scatter(best_centers[:, 0], best_centers[:, 1], marker='+', c='gold', s=40)

plt.show()
