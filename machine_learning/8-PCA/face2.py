# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:58:51 2018

@author: Administrator
未进行降维的SVC模型
"""

import numpy as np
import sklearn.datasets as sd
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as plt

faces = sd.fetch_olivetti_faces('../ML/data/')
x = faces.data                              # 照片
y = faces.target                            # lable 人名,编号表示
train_x, test_x, train_y, test_y = ms.train_test_split(x,y,
                                                       test_size=0.2, 
                                                       random_state=7
                                                       )
model = svm.SVC(class_weight='balanced')
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / len(pred_test_y))     # 0.1875
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