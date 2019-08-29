# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:10:41 2018

@author: Administrator
"""
'''
sn.NearestNeighbors(n_neighbors=邻居数,
                     algorithm=算法,              # 'ball_tree'
                     )
    --> return: FNN模型
                FNN模型.fit(已知样本集合)
                            xxx...xxx   --> row_11
                            ...
                            xxx...xxx   --> row_23
                            ...
                FNN模型.kneighbors(待求样本集合)
                                    xxx...xxx  11 23 34 (近邻下标索引) 0.5 0.3 0.1 (近邻距离)
                                    xxx...xxx  22 10 15 (近邻下标索引) 0.4 0.2 0.1 (近邻距离)
                                    ...
                    --> return: 与待求样本近邻的多个已知样本与待求样本的距离矩阵
                                与待求样本近邻的已知样本下标索引矩阵
代码：FNN.py
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpc   # 图形对象块：包括常见图形如多边形，矩形圆形等
import sklearn.neighbors as sn

train_x = np.array([[6,7],[4.7,8.5],[2,7],[2,5],[3.4,3],[6,2],
                   [4,8],[10,5],[10,7],[8.6,8.5],[7.3,8.5]])

# 找最近邻点
model = sn.NearestNeighbors(n_neighbors=5,                  # 近邻个数
                            algorithm='ball_tree'           # 算法
                            )
model.fit(train_x)

test_x = np.array([[5,7],[3.7,5.5],[2.5,6],[3,5],[6.4,3],[6.5,4],
                   [3,8],[6,4],[5,6],[4.6,8.5],[8.3,6.5]])
nn_distance, nn_indices = model.kneighbors(test_x)
print('nn_distance:',nn_distance,'nn_indices:',nn_indices, sep='\n')

plt.figure('Find Nearest Neighbors', facecolor='lightgray')
plt.title('Find Nearest Neighbors', fontsize=14)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)

plt.scatter(train_x[:, 0], train_x[:, 1], c='k', s=30, zorder=2)


cs = plt.get_cmap('gist_rainbow', len(nn_indices))(range(len(nn_indices)))
#print(plt.get_cmap('gist_rainbow', len(nn_indices))(0))
#print(plt.get_cmap('gist_rainbow', len(nn_indices))(1))
#print(plt.get_cmap('gist_rainbow', len(nn_indices))(2))
#print(plt.get_cmap('gist_rainbow', len(nn_indices))(3))
for i, (x, nn_index) in enumerate(zip(test_x, nn_indices)):
#    nn_index = nn_indices[i]
#    x = test_x[i]
    # mpc.Polygon  多边形
    plt.gca().add_patch(mpc.Polygon(train_x[nn_index], ec='none', fc=cs[i], alpha=0.5))
    plt.scatter(x[0], x[1], c=cs[i], s=80, zorder=1)

plt.axis('equal')                       # ?????????????
plt.show()



'''
nn_distance:
[[1.         1.41421356 1.52970585]  # test_x[0]与最近邻的三个train_x样本点的距离
 [1.77200451 2.26715681 2.51793566]
 [1.11803399 1.11803399 2.5       ]
 [1.         2.03960781 2.23606798]
 [1.07703296 3.         4.01995025]
 [2.06155281 3.04138127 3.25729949]
 [1.         1.41421356 1.77200451]
 [2.         2.78567766 3.        ]
 [1.41421356 1.41421356 2.53179778]
 [0.1        0.78102497 2.05182845]
 [1.77200451 2.02237484 2.23606798]]
nn_indices:
[[ 0  6  1]    # 与test_x[0]最近邻的三个train_x的样本点的索引
 [ 3  2  4]
 [ 2  3  6]
 [ 3  4  2]
 [ 5  4  0]
 [ 5  0  4]
 [ 6  2  1]
 [ 5  4  0]
 [ 8  7  9]
 [ 1  6  0]
 [ 8  9 10]]
'''

'''
class NearestNeighbors(NeighborsBase, KNeighborsMixin, RadiusNeighborsMixin, UnsupervisedMixin):
    Parameters
    ----------
    n_neighbors : int, optional (default = 5)
        Number of neighbors to use by default for :meth:`kneighbors` queries.
    algorithm : {'auto', 'ball_tree', 'kd_tree', 'brute'}, optional
        Algorithm used to compute the nearest neighbors:
        - 'ball_tree' will use :class:`BallTree`
        - 'kd_tree' will use :class:`KDTree`
        - 'brute' will use a brute-force search.
        - 'auto' will attempt to decide the most appropriate algorithm
          based on the values passed to :meth:`fit` method.
'''

'''
get_cmap(name=None, lut=None)
    Get a colormap instance, defaulting to rc values if *name* is None.
    
    Colormaps added with :func:`register_cmap` take precedence over
    built-in colormaps.
    
    If *name* is a :class:`matplotlib.colors.Colormap` instance, it will be
    returned.
    
    If *lut* is not None it must be an integer giving the number of
    entries desired in the lookup table, and *name* must be a standard
    mpl colormap name.
'''

'''
axis(*v, **kwargs)
    Convenience method to get or set axis properties.
    
    Calling with no arguments::
    
axis()
    
    returns the current axes limits ``[xmin, xmax, ymin, ymax]``.::
    
axis(v)
    
    sets the min and max of the x and y axes, with
    ``v = [xmin, xmax, ymin, ymax]``.::
    
axis('off')
    
    turns off the axis lines and labels.::
    
axis('equal')
    
    changes limits of *x* or *y* axis so that equal increments of *x*
    and *y* have the same length; a circle is circular.::
    
axis('scaled')
    
    achieves the same result by changing the dimensions of the plot box instead
    of the axis data limits.::
    
axis('tight')
    
    changes *x* and *y* axis limits such that all data is shown. If
    all data is already shown, it will move it to the center of the
    figure without modifying (*xmax* - *xmin*) or (*ymax* -
    *ymin*). Note this is slightly different than in MATLAB.::
    
axis('image')
    
    is 'scaled' with the axis limits equal to the data limits.::
    
axis('auto')
    
    and::
    
axis('normal')
    
    are deprecated. They restore default behavior; axis limits are automatically
    scaled to make the data fit comfortably within the plot box.
    
    if ``len(*v)==0``, you can pass in *xmin*, *xmax*, *ymin*, *ymax*
    as kwargs selectively to alter just those limits without changing
    the others.
    
axis('square')
    
    changes the limit ranges (*xmax*-*xmin*) and (*ymax*-*ymin*) of
    the *x* and *y* axes to be the same, and have the same scaling,
    resulting in a square plot.
    
    The xmin, xmax, ymin, ymax tuple is returned
    
    .. seealso::
    
        :func:`xlim`, :func:`ylim`
           For setting the x- and y-limits individually.
'''