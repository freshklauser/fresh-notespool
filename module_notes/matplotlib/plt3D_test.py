# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-06-14 14:35:39
# @Last Modified by:   klaus
# @Last Modified time: 2019-06-14 16:57:34


'''
# zdir : {'x', 'y', 'z'}
        When plotting 2D data, the direction to use as z ('x', 'y' or 'z');
        defaults to 'z'.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = np.arange(20)
ysarr = np.random.rand(80) * 100
ysarr = ysarr.reshape((4, -1))
print(ysarr.shape)
for i, c, z in zip([0, 1, 2, 3], ['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
    ys = ysarr[i]
    # cs = [c] * len(xs)          # colormap
    # cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', alpha=0.8)    # color=cs
    # zdir='y': Z数据显示在原始3维坐标系的Y轴上
ax.set_xlabel('time')
ax.set_ylabel('freq')
ax.set_zlabel('amplitude')
plt.show()
