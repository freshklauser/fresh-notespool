# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-29 10:26:16
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-02-29 20:17:34

import scipy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.arange()
np.angle()


A = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]]
row = len(A)

for i in range(row):
    if max(A[i]) == 1:
        j = A[i].index(1)
        print(i, j, A[i][j])
        break
