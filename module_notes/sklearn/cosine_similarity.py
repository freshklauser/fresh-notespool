# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-04-03 16:17:33
# @Last Modified by:   F1684324
# @Last Modified time: 2019-07-05 09:06:20


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

# Method1: cosine_similarity
a = np.array([[10, 1, 2], [23, 10, 9]])
b = np.array([[1, 2, 5], [34, 2, 12], [1, 50, 30]])


# a = [[1, 3, 2], [2, 2, 1]]
cos_sim = cosine_similarity(a, b)
print(cos_sim)

# Method2: pairwise_distances ==> returns a distance matrix
# pairwise_distances(X, Y=None, metric='euclidean', n_jobs=1, **kwds) ==> eulidean distance / cosin
#         metric='euclidean' ==> eulidean distance
#         metric='cosine' ==> cosine distance (cos_sim = 1 - cosine_distance)
# metric: scikit-learn: ['cityblock', 'cosine', 'euclidean', 'l1', 'l2','manhattan']
#         scipy.spatial.distance: ['braycurtis', 'chebyshev, 'correlation', 'hamming', 'jaccard'...]
cos_sim_1 = 1 - pairwise_distances(a, b, metric='cosine')
print(cos_sim_1 == cos_sim)
