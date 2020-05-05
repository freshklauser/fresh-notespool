# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-29 10:26:16
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-13 20:54:21


# import scipy
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

import numpy as np


def max_substrarg(word_a, word_b):
    arr = np.zeros((len(word_a), len(word_b)), dtype=np.int)    # grid
    for i in range(len(word_a)):
        for j in range(len(word_b)):

            if word_a[i] == word_b[j]:               # if...else... 核心逻辑
                arr[i, j] = arr[i - 1, j - 1] + 1
            else:
                arr[i, j] = max(arr[i - 1, j], arr[i, j - 1])

    return arr

# np.angle()


# A = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
#      [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]]
# row = len(A)


# for i in range(row):
#     if max(A[i]) == 1:
#         j = A[i].index(1)
#         print(i, j, A[i][j])
#         break

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


if __name__ == '__main__':
    word_a = "atachee"
    word_b = "cats"
    res = max_substrarg(word_a, word_b)
    print(res)
