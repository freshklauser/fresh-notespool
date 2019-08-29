# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:58:51 2018
@author: Administrator
先根据优选的最佳维度进行PCA降维；
对降维后的数据进行训练，采用SVM模型
降维前后的precision变化明显
"""

import numpy as np
import sklearn.datasets as sd
import sklearn.decomposition as dc              # 降维后采用SVM模型
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as plt

faces = sd.fetch_olivetti_faces('../ML/data/')
x = faces.data                              # 照片
y = faces.target                            # lable 人名,编号表示

model = dc.PCA(n_components=140)            # 指定降维后的维度
pca_x = model.fit_transform(x)              # PCA模型对样本x进行降维
print(x.shape, pca_x.shape)                 # (400, 4096) --> 降维后 (400, 140)

# 对样本特征降维  (线性拟合时，采用多项式扩展器进行特征升维)
# 核函数：升维
# 主成分分析PCA: 降维
train_x, test_x, train_y, test_y = ms.train_test_split(pca_x,           # 训练样本train_x采用降维后的样本
                                                       y, 
                                                       test_size=0.2, 
                                                       random_state=7
                                                       )
model = svm.SVC(class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / len(pred_test_y))
# train_x = x: 0.1875  (即降维前的precision)
# train_x = pca_x : 0.975 (即降维后的precision)

# 分类报告 
print(sm.classification_report(test_y, pred_test_y))

# 混淆矩阵: 以实际类别为行，以预测类别为列
confuse_matrix = sm.confusion_matrix(test_y, pred_test_y)

plt.figure('Confusion_Matrix')
plt.title('Confusion_Matrix')
plt.xlabel('Predicted Class')           # 预测类别为列
plt.ylabel('True Class')                # 实际类别为行
plt.tick_params(labelsize=10)
plt.imshow(confuse_matrix,
           interpolation='nearest',
           cmap='gray'
           )
plt.show()