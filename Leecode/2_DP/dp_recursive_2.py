# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-04 18:36:56
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-14 19:36:02

'dp的解决方法之一：选择 or 不选择'
'''
题目： arr = [3,34,4,12,5,2], 在列表中选出若干数字，使其相加为 S=20,存在返回True

递归转移关系：
subset(i, s): i-当前看第i个数字，s-加和为s
      例如：i=5          subset(arr[5], 9)
                  （选i=5）|          |（不选i=5）
     subset(arr[4], s-arr[5])   or   subset(arr[4], s)

递归终止条件：
    - 1）subset(arr[k], 0): s-arr[j]==0已经存在了，return True即可
        if s == 0: return True
    - 2）subset(arr[1], 3): s-arr[j]=3, 则只有arr[0]=3时才返回True
        if i == 0: return arr[0] == s
    - 3）若选择i,左边情况 subset(arr[i], 12): 12 > 9, 左边的情况永远不会满足相加s=20
        if arr[i] > s: return Fasle
'''
import numpy as np


def rec_subset(arr, i, s):
    ' -- Method1: 递归算法 -- '
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:          # 选i的情况不会满足条件，可直接剪枝，只返回右边不选i的情况
        return rec_subset(arr, i - 1, s)
    else:
        A = rec_subset(arr, i - 1, s - arr[i])      # ***** 选i的情况
        B = rec_subset(arr, i - 1, s)             # ***** 不选i的情况
        return A or B


def db_subset(arr, s):
    ' -- Method2: dp算法 --  | ---> 见截图'
    # 用二维数组保存所有中间所有的动态过程(overlap subset)  --->
    subset = np.zeros((len(arr), s + 1), dtype=bool)
    # 所有出口
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for k in range(1, s + 1):
            if arr[i] > k:                        # 剪枝左边选i的情况
                subset[i, k] = subset[i - 1, k]
            else:
                A = subset[i - 1, k - arr[i]]     # 选i
                B = subset[i - 1, k]              # 不选i
                subset[i, k] = A or B
    r, c = subset.shape
    return subset[r - 1, c - 1]


if __name__ == '__main__':
    arr = [1, 2, 4, 1, 7, 8, 3]
    # res = db_opt(arr)
    # res = rec_subset(arr, len(arr)-1, 11)
    res = db_subset(arr, 11)
    print(res)
    print(np.random.randint(10, 100, 10, int))
