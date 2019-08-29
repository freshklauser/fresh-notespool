# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:38:12 2018
@author: Administrator
根据还原率确定最佳降维后的维度
"""

import sklearn.datasets as sd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.decomposition as dc

# 加载数据集
faces = sd.fetch_olivetti_faces('../ML/data/')
x = faces.data                              # 照片
y = faces.target                            # lable 人名,编号表示
print(x.shape)                              # (400, 4096)  400个样本，每个样本4096个特征
print(np.unique(y))                         # [0 1 2 3 4 ...] .unique去重且排序

# 成分数
ncompns = range(10, 600, 10)                # 降维后的维度取值范围 range(start, stop[, step]) -> range object
evrs = []                                   # 还原率
for ncompn in ncompns:
    model = dc.PCA(n_components=ncompn)             # PCA模型
    model.fit_transform(x)
    evr = model.explained_variance_ratio_.sum()     # 还原率   
    evrs.append(evr)
plt.figure('Explained_Variance_Ratio')
plt.title('Explained_Variance_Ratio')
plt.xlabel('n_compoments')
plt.ylabel('Explained_Variance_Ratio')
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.plot(ncompns, evrs, c='dodgerblue', label='Explained_Variance_Ratio')
plt.legend()
plt.show()

## 显示label-faceimage 矩阵图 imshow / matshow  左上角坐标0点
#plt.figure('Olivetti Faces')
#plt.subplots_adjust(left=0.04, bottom=0,    # 左边距，底边距
#                    right=0.98, top=0.96,   # 右边距= 1-0.98， 顶边距 = 1-0.96
#                    wspace=0,               # 水平之间图片空白
#                    hspace=0                # 水平之间图片不留空白
#                    )
#rows, cols = 10, 40
#for row in range(rows):
#    for col in range(cols):
#        plt.subplot(rows, cols, 
#                    row * cols + col + 1   # 图号
#                    )
#        plt.title(str(col), fontsize=8, color='limegreen')
#        if col == 0:
#            plt.ylabel(str(row), fontsize=8, color='limegreen')
#        plt.xticks(())
#        plt.yticks(())                      # 关闭刻度
#        image = x[y == col][row].reshape(64, 64)
#                                            # 
#        plt.imshow(image, cmap='gray')
#plt.show()