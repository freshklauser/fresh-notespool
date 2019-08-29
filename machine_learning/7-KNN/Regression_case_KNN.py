# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:05:33 2018

@author: Administrator
"""
'''
基于KNN的回归：
只能做训练集范围内的回归预测，且没有解析解，没有解析函数 
'''

import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as plt

train_x = np.random.rand(100, 1) * 10 - 5 
train_y = np.sinc(train_x).ravel()                      # 扁平化，y只有1列
train_y += 0.2 * (0.5 - np.random.rand(train_y.size))   # 增加随机噪声

model = sn.KNeighborsRegressor(n_neighbors=10,          # 越大，需要越多的点平均，不敏感，线条钝化； 越小，敏感度大，波动性越大
                               weights='distance'
                               )
model.fit(train_x, train_y)

test_x = np.linspace(-5, 5 , 10000).reshape(-1, 1)
test_y = np.sinc(test_x).ravel()
pred_test_y = model.predict(test_x)



plt.figure('KNN_Regression', facecolor='lightgray')
plt.title('KNN_Regression', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.scatter(train_x, train_y, s=60, c='b')
plt.plot(test_x, test_y, '--', c='g', linewidth=2, label='Testing')
plt.plot(test_x, pred_test_y, '-', c='r', linewidth=2, label='Predicted Testing')
plt.legend()
plt.show()




'''
np.random.rand(3,2)
    array([[ 0.14022471,  0.96360618],  #random
           [ 0.37601032,  0.25528411],  #random
           [ 0.49313049,  0.94909878]]) #random
'''


'''
model = sn.KNeighborsClassifier
    Parameters
    ----------
    n_neighbors : int, optional (default = 5)
        Number of neighbors to use by default for :meth:`kneighbors` queries.

    weights : str or callable, optional (default = 'uniform')
        weight function used in prediction.  Possible values:

        - 'uniform' : uniform weights.  All points in each neighborhood
          are weighted equally.
        - 'distance' : weight points by the inverse of their distance.
          in this case, closer neighbors of a query point will have a
          greater influence than neighbors which are further away.
        - [callable] : a user-defined function which accepts an
          array of distances, and returns an array of the same shape
          containing the weights.

    algorithm : {'auto', 'ball_tree', 'kd_tree', 'brute'}, optional
        Algorithm used to compute the nearest neighbors:

        - 'ball_tree' will use :class:`BallTree`
        - 'kd_tree' will use :class:`KDTree`
        - 'brute' will use a brute-force search.
        - 'auto' will attempt to decide the most appropriate algorithm
          based on the values passed to :meth:`fit` method.

        Note: fitting on sparse input will override the setting of
        this parameter, using brute force.
'''
