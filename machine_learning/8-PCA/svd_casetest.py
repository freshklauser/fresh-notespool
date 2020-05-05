# -*- coding: utf-8 -*-
# @Author: Klaus
# @Date:   2019-05-19 20:29:26
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-16 14:34:52
# blog contents: https://blog.csdn.net/xiaocong1990/article/details/54909126

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.set_printoptions(precision=2)

reader = pd.read_csv(r'svd_casetest.csv', index_col=None, header=None)
data = np.array(reader)
# print(data.shape)

# svd
U, sigma, VT = np.linalg.svd(data)
print(U.shape)
print(sigma.shape, sigma)       # (9,)
# sigma_mat = np.diag(sigma)    # (9,9)
print(VT.shape)
# dimension = 3
feature = U[:, :3] * -1
sample = VT[:3, :] * -1
print(feature.shape)
print(sample.shape)

# plot data with 2D(2cols of feature, 2rows of sample)
plt.figure()
plt.scatter(feature[:, 1], feature[:, 2], marker='o', c='red')
plt.scatter(sample[1, :], sample[2, :], marker='+', c='blue')
plt.show()

# restore the data
# 由于U和sigma维度不一致，还原时需手动将对角矩阵行补0，与U维度一致
# U S VT --> (11,11) (11,9) (9,9)
S = np.zeros([U.shape[0], sigma.shape[0]])
for i in range(sigma.shape[0]):
    S[i, i] = sigma[i]
print(U.shape, S.shape)
# A = U*S*VT
temp = np.dot(U, S)
data_restore = np.dot(temp, VT).astype(int)
print(data)
print(data_restore)
print(data_restore == data)
