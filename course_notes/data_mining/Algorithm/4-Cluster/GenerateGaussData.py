# -*- coding: utf-8 -*-
# @Author: Klaus
# @Date:   2019-06-16 21:56:39
# @Last Modified by:   Klaus
# @Last Modified time: 2019-06-16 22:44:00

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


mu = ([0.2, 1], [1, 2], [1.2, 1.0], [0.8, 0.5])
stdval = ([0.1, 0.3], [0.2, 0.1], [0.1, 0.2], [0.05, 0.16])
dim = (1000, 2)
# Generate Gauss Distribution data
data1 = np.random.normal(loc=mu[0], scale=stdval[0], size=dim)
data2 = np.random.normal(loc=mu[1], scale=stdval[1], size=dim)
data3 = np.random.normal(loc=mu[2], scale=stdval[2], size=dim)
data4 = np.random.normal(loc=mu[3], scale=stdval[3], size=dim)
# Merge data generated to an array
data = np.vstack([data1, data2, data3, data4])
# data save to csv for cluster algorithm
df = pd.DataFrame(data)
df.to_csv('cluster_data.csv', header=False, index=False, mode='w')


# plot
plt.figure()
# plt.scatter(data1[:, 0], data1[:, 1], s=5, c='r')
# plt.scatter(data2[:, 0], data2[:, 1], s=5, c='g')
# plt.scatter(data3[:, 0], data3[:, 1], s=5, c='b')
# plt.scatter(data4[:, 0], data4[:, 1], s=5, c='purple')
plt.scatter(data[:, 0], data[:, 1], s=2, c='purple')
plt.savefig('cluster_data.jpg', dpi=100)
plt.show()
