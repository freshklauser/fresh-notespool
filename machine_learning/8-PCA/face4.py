# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 09:38:12 2018
@author: Administrator
# 维度递减，观察不同主成分样本还原后与原图像差异
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


# 显示label-faceimage 矩阵图 imshow / matshow  左上角坐标0点
plt.figure('Explained_Variance_Ratio')
plt.subplots_adjust(left=0.04, bottom=0,    # 左边距，底边距
                    right=0.98, top=0.96,   # 右边距= 1-0.98， 顶边距 = 1-0.96
                    wspace=0,               # 水平之间图片空白
                    hspace=0                # 水平之间图片不留空白
                    )
rows, cols = 11, 40
for row in range(rows):
    if row > 0:                             # 第一行是原图
        ncompn = 140 - (row - 1)* 15        # face3.py确定ncompn=140是曲线明显变化拐点
                                            # 维度递减，观察不同主成分样本还原后与原图像差异
        '''
        # 第一行是原图
        # face3.py确定ncompn=140是曲线明显变化拐点
        # 维度递减，观察不同主成分样本还原后与原图像差异
        '''
        model = dc.PCA(n_components=ncompn)
        model.fit_transform(x)
    for col in range(cols):
        plt.subplot(rows, cols, 
                    row * cols + col + 1   # 图号
                    )
        plt.title(str(col), fontsize=8, color='limegreen')
        if col == 0:
            plt.ylabel(str(ncompn) if row > 0 else 'orig', fontsize=8, color='limegreen')
        plt.xticks(())
        plt.yticks(())                      # 关闭刻度
        if row > 0:
            pca_x = model.transform([x[y == col][0]])
            ipca_x = model.inverse_transform(pca_x)
            image = ipca_x.reshape(64, 64)              # 降维后还原样本
        else:
            image = x[y == col][0].reshape(64, 64)
        plt.imshow(image, cmap='gray')
plt.show()