# -*- coding: utf-8 -*-
# @Author: Klaus
# @Date:   2019-06-16 21:56:39
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-09-03 11:36:30

'''[Generate Gaussian distribution data]

normal(...) method of mtrand.RandomState instance
    normal(loc=0.0, scale=1.0, size=None)

    Draw random samples from a normal (Gaussian) distribution.

    Parameters
    ----------
    loc : float or array_like of floats
        Mean ("centre") of the distribution.
    scale : float or array_like of floats
        Standard deviation (spread or "width") of the distribution.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  If size is ``None`` (default),
        a single value is returned if ``loc`` and ``scale`` are both scalars.
        Otherwise, ``np.broadcast(loc, scale).size`` samples are drawn.

    Returns
    -------
    out : ndarray or scalar
        Drawn samples from the parameterized normal distribution.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# code updating further goes to 4-cluster directory


mu = ([0.2, 1], [1, 2], [1.2, 1.0], [0.8, 0.5])
stdval = ([0.1, 0.3], [0.2, 0.1], [0.1, 0.2], [0.05, 0.16])
dim = (1000, 2)
data1 = np.random.normal(loc=mu[0], scale=stdval[0], size=dim)
data2 = np.random.normal(loc=mu[1], scale=stdval[1], size=dim)
data3 = np.random.normal(loc=mu[2], scale=stdval[2], size=dim)
data4 = np.random.normal(loc=mu[3], scale=stdval[3], size=dim)
data = np.vstack([data1, data2, data3, data4])
# data save to csv for cluster algorithm
# df = pd.DataFrame(data)
# df.to_csv()

print(data.shape)
# plot
plt.figure()
# plt.plot([1,2,3], [11,22,33])
# plt.scatter(data1[:, 0], data1[:, 1], s=5, c='r')
# plt.scatter(data2[:, 0], data2[:, 1], s=5, c='g')
# plt.scatter(data3[:, 0], data3[:, 1], s=5, c='b')
# plt.scatter(data4[:, 0], data4[:, 1], s=5, c='purple')
plt.scatter(data[:, 0], data[:, 1], s=2, c='purple')
plt.show()
