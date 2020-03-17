# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-04 18:36:56
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 22:56:57

'''
dp的解决方法之一：选择 or 不选择
例如： [1,2,4,1,7,8,3],如何计算出不相邻的数的和的最大值

思路：如果以A[i]结尾, 怎么求最大值 --> 递归
    构建 opts = [], opt[i]存储的是以到索引i为止的可能组合相加的最大值,避免在递归过程中重复计算opt[j]的子问题
    相当于构建一个以arr元素为横坐标，以range(len(arr))元素为纵坐标的二维表
递归转移关系：
    以i=5，即A[5]=8为例，可以如下考虑：
        如果选择i=5作为最后一个数字的组合：
            opt[i] = opt[i-2] + A[5]     ***** 选择i=5的元素
        如果不选i=5为最后一个数字的组合：
            opt[i] = opt[i-1]            ***** 不选择i=5的元素
递归终止条件：
    1）只有1个元素，opt[0] = A[0]
    2）只有2个元素，opt[0] = max(A[0], A[1])
'''


def db_opt(arr):
    ' -- Method1: dp算法 -- '
    # 初始化opt辅助列表,存储相加的结果  ---> 这里也可以用字典, db[arr[i]] = {}, db[arr[i]][j] = val
    # i为arr的索引，j为range(len(arr))的元素
    dp = [0] * len(arr)

    # 特殊情况单列：递归终止条件
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(len(arr)):
        A = dp[i - 2] + arr[i]
        B = dp[i - 1]
        dp[i] = max(A, B)
    return dp[-1]


def rec_opt(arr, i):
    ' -- Method2: 递归算法 -- '
    rec_opt = [0] * len(arr)
    # 递归终止条件
    if i == 1:
        return arr
    elif i == 2:
        return max(arr[0], arr[1])
    else:
        # 递归转换关系
        A = rec_opt(arr, i - 2) + arr[i]
        B = rec_opt(arr, i - 1)
    return max(A, B)


if __name__ == '__main__':
    arr = [1, 2, 4, 1, 7, 8, 3]
    # res = db_opt(arr)
    res = rec_opt(arr)
    print(res)
