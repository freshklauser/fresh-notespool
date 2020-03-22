# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-29 10:26:16
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-13 20:54:21

# import scipy
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# np.arange()
# np.angle()


# A = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
#      [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]]
# row = len(A)

# for i in range(row):
#     if max(A[i]) == 1:
#         j = A[i].index(1)
#         print(i, j, A[i][j])
#         break


def password(s):
    n = len(s)
    for i in range(n):
        # A --> Z
        if "A" <= s[i] < "Z":
            s[i] = chr(ord(s[i] + 1)).lower()
        if s[i] == "Z":
            s[i] = "a"
        if "a" <= s[i] < "z":
            s[i] = chr(ord(s[i] + 1)).upper()
        if s[i] == "Z":
            s[i] = "a"
