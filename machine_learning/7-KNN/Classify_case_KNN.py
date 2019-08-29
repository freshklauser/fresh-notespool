# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 14:05:33 2018

@author: Administrator
"""
'''
基于KNN的有监督分类
'''

import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as plt

train_x, train_y = [], []
with open('knn.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr in line[:-1].split(',')]
        train_x.append(data[:-1])
        train_y.append(data[-1])
train_x = np.array(train_x)
train_y = np.array(train_y, dtype=int)

# KNN_Classifier模型
model = sn.KNeighborsClassifier(n_neighbors=10,
                                weights='distance'
                                )

'''
KNN模型区别于其他模型的地方之一：模型训练属于惰性学习，只保存数据，
在预测时才进行计算近邻距离, 即模型训练和预测在.predict阶段同时完成
'''
model.fit(train_x, train_y)



l, r, h = train_x[:, 0].min() - 1, train_x[:, 0].max() + 1, 0.005
b, t, v = train_x[:, 1].min() - 1, train_x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]        # 转化为模型输入和输出需要的格式，一行一样本，一列一标签
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

# test_set
test_x = np.array([[2.2,6.2],[3.6,1.8],[4.5,3.6]])
pred_test_y = model.predict(test_x)

'''
def kneighbors(self, X=None, n_neighbors=None, return_distance=True):
    Finds the K-neighbors of a point.
    Returns indices of and distances to the neighbors of each point. (注意return值顺序)
'''
nn_distance, nn_indices = model.kneighbors(test_x)
print('nn_distance:',nn_distance,'nn_indices:',nn_indices, sep='\n')
#nn_distance:
#[[0.4936598  0.64776539 0.66370174 0.73824115 0.73979727 0.74094534
#  0.74953319 0.79195959 0.80305666 0.82292162]
# [0.43324358 0.57384667 0.57801384 0.65       0.76321688 0.83677954
#  0.8832327  0.9060905  0.94894678 1.00404183]
# [0.55542776 0.75213031 0.7823682  0.93150416 0.99322706 1.11305885
#  1.11682586 1.12361025 1.1461239  1.18680243]]
#nn_indices:
#[[139  25  91 118 124  40  82 142  52  22]
# [132 111  47 102  95  87  42 138  39 140]
# [ 92  79 119  64 128 131  44  77  23  83]]


plt.figure('KNN Nearest Neighbors', facecolor='lightgray')
plt.title('KNN Nearest Neighbors', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)
# 绘制伪彩图
plt.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')

'''
返回类别数组中的去重类别：
def unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None):
    Find the unique elements of an array.
    Returns the sorted unique elements of an array.
    默认返回经过排序后的唯一元素数组。(可接受其他return值，需要设置True)
'''
classes = np.unique(train_y)               # [0 1 2] ,类别去重并排序, 不需要calsses.sort()
#classes.sort()

'''
构建色级，注意用法：plt.get_cmap(..)(..)
个人理解:
    plt.get_cmap('brg', len(classes)) : <class 'matplotlib.colors.LinearSegmentedColormap'>
    plt.get_cmap(name=.., lut=..): 色级
        如果lut非空，则lut必须是查找表中需要的条目的整数，且name必须是表中的colormap的名字
    plt.get_cmap(..)(range(n)):   ---> type: numpy.array
        n为数组的长度，不能小于色级的条目数lut, 最佳是 == 分类类别数(类别和色级带一一对应),
        n < lut, 后续会报错index is out of bouds
'''
cs = plt.get_cmap('brg', len(classes))(range(len(classes)))  # 数组,调用色带正常的数组索引即可
print(type(cs))                                       # <class 'numpy.ndarray'>

'''
绘制分类且对应颜色标记的散点图
'''
plt.scatter(train_x[:, 0], train_x[:, 1], c=cs[train_y], s=30)
plt.scatter(test_x[:, 0], test_x[:, 1], c=cs[pred_test_y], s=30, marker='+', )

'''
找出每个测试点周围的n_neighbors个临近点 并进行与测试点颜色对应的色彩标记
'''
for nn_indice, y in zip(nn_indices, pred_test_y):
    plt.scatter(train_x[nn_indice, 0],                      # x坐标
                train_x[nn_indice, 1],                      # x坐标
                edgecolor=cs[np.ones_like(nn_indice)*y],    # np.ones_like(..)*y: 近邻点颜色与test点保持一致
                facecolor='none',                           # 填充色空白
                marker='D', s=70
                )
    print(nn_indice)
    print(y, np.ones_like(nn_indice)*y)
#    [139  25  91 118 124  40  82 142  52  22] -- nn_indice
#    1 [1 1 1 1 1 1 1 1 1 1]
#    [132 111  47 102  95  87  42 138  39 140] -- nn_indice
#    0 [0 0 0 0 0 0 0 0 0 0]
#    [ 92  79 119  64 128 131  44  77  23  83] -- nn_indice
#    2 [2 2 2 2 2 2 2 2 2 2]

plt.show()



'''
备注：
    def kneighbors(self, X=None, n_neighbors=None, return_distance=True):
        """Finds the K-neighbors of a point.

        Returns indices of and distances to the neighbors of each point.

        Parameters
        ----------
        X : array-like, shape (n_query, n_features), \
                or (n_query, n_indexed) if metric == 'precomputed'
            The query point or points.
            If not provided, neighbors of each indexed point are returned.
            In this case, the query point is not considered its own neighbor.
        n_neighbors : int
            Number of neighbors to get (default is the value
            passed to the constructor).
        return_distance : boolean, optional. Defaults to True.
            If False, distances will not be returned

        Returns
        -------
        dist : array
            Array representing the lengths to points, only present if
            return_distance=True

        ind : array
            Indices of the nearest points in the population matrix.
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

'''
def get_cmap(name=None, lut=None):
    """
    Get a colormap instance, defaulting to rc values if *name* is None.

    Colormaps added with :func:`register_cmap` take precedence over
    built-in colormaps.

    If *name* is a :class:`matplotlib.colors.Colormap` instance, it will be
    returned.

    If *lut* is not None it must be an integer giving the number of
    entries desired in the lookup table, and *name* must be a standard
    mpl colormap name.
'''