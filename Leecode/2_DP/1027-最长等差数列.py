# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-01 17:04:13
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 14:35:44

# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000
# A = [3,6,9,12,18]
from collections import defaultdict
"""
defaultdict的用法需要重视, 整合相同的key，并把该key对应的所有value放再同一个列表下(如果定义的类型是List)
>>> A = [2,2,4,14,2,2]
>>> for i, num in enumerate(A):
...     mapping[num].append(i)
...
>>> mapping
defaultdict(<class 'list'>, {2: [0, 1, 4, 5], 4: [2], 14: [3]})
>>> mapping[2]
[0, 1, 4, 5]        # A中2的所有索引按顺序分别是0,1,4,5
"""


class Solution:
    """
    动态规划思路：以每个元素作为等差数列终点，计算出该数列长度，选择出最大值返回即可。
    在每个位置上，以字典结构保存该位置元素与前面每个位置上元素的差值，与对应该差值的数列长度。
    """

    def longestArithSeqLength(self, A):
        n = len(A)
        max_len = 2

        # dp[i]: A[i]表示以A[i]为等差数列终点
        # dp[i] = {}, {}的key为A[i]为终点的等差数列的差值diff,value表示该等差数列的长度
        dp = [{} for _ in range(n)]

        # 注意双重循环的start和end, i为被减数的索引，j为减数的索引，j<i
        for i in range(1, n):
            for j in range(i):
                k = A[i] - A[j]         # 差值 = 后值 - 前值
                # dp[j].get(k, 1)：字典dp[j]如果存在key=k,返回对应value，否则返回默认值1
                m = dp[j].get(k, 1) + 1
                dp[i][k] = m
            max_len = max(max_len, max(dp[i].values()))
        return max_len


class Solution2:
    def longestArithSeqLength(self, A):
        n = len(A)
        max_length = 2
        # 建立字典储存A的信息，key是A的数值，val是这个数值的index的列表
        mapping = defaultdict(list)
        for i, val in enumerate(A):
            mapping[val].append(i)
        # 两层遍历：对于每个i，j看以A[i],A[j]为前两项的等差数列有几项
        # 关注点：指向j的指针的位置, 下一个等差数列值需要在当前值的index以后的列表中查找
        for i in range(0, n):
            for j in range(i + 1, n):
                length = 2
                diff = A[j] - A[i]                      # 差值 = 后 - 前
                while True:
                    next_val = A[j] + diff              # next value
                    if next_val not in mapping.keys():  # 查找 next_val 是否在 j 之后的索引对应的列表中
                        break
                    for_tag = False                     # 标示 是否在mapping[next_val]的索引列表中找到index>j: true 找到
                    for index in mapping[next_val]:     # 在列表中，则遍历mapping，找到大于j的索引，更新j为该索引
                        if index > j:
                            j = index                   # 更新索引后退出该层循环，继续 while loop
                            length += 1
                            max_length = max(max_length, length)
                            for_tag = True
                            break
                    if not for_tag:                     # 找到index>j，继续 while loop,否则退出while
                        break
        return max_length


if __name__ == '__main__':
    # A = [2,2,4,14,2,2]
    # A = [3,6,9,12,18,9]
    # A = [83,20,17,43,52,78,68,45]
    A = [25, 78, 45, 27, 75, 10, 90, 77, 60, 8, 43, 5, 55, 47, 57, 17, 8, 63, 18, 69, 63, 87, 35, 19, 78, 42, 25, 27, 24, 23, 88, 56, 14, 42, 16, 64, 8, 62, 48, 76, 66, 75, 59, 43, 16, 11, 15, 41, 20, 34,
         69, 69, 58, 42, 22, 27, 79, 81, 63, 59, 57, 51, 11, 48, 89, 29, 30, 79, 40, 87, 17, 24, 16, 82, 18, 9, 86, 9, 90, 74, 17, 21, 8, 18, 24, 62, 8, 31, 84, 56, 70, 59, 55, 22, 44, 31, 11, 82, 80, 38]
    # A = [24,1,1,100,1,1,2,3,4,5,6,7,8,9,94,0,17,0, 1]
    # A = [1,3,2,4,7,6,5,12,7,8,9,7,3,5,11,14,16]
    # A = [20,1,15,3,10,5,8]
    # A = [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]

    output = Solution().longestArithSeqLength(A)
    print(output)

    from collections import defaultdict

    a = [1, 2, 3, 1, 3, 5, 7, 6, 8, 6]


# original:
# class Solution2:
#     def longestArithSeqLength(self, A):
#         n = len(A)
#         max_length = 2
#         # 建立字典储存A的信息，key是A的数值，val是这个数值的index的列表
#         mapping = defaultdict(list)
#         for i, val in enumerate(A):
#             mapping[val].append(i)
#         # print(mapping)
#         # 两层遍历：对应 diff = A[j] - A[i] 中的i 和 j（差值 = 后 - 前 --> j > i）
#         # 关注点：指向j的指针的位置, 下一个等差数列值需要在当前值的index以后的列表中查找
#         for i in range(0, n):
#             for j in range(i + 1, n):
#                 length = 2
#                 diff = A[j] - A[i]
#                 flag = True
#                 while flag:
#                     next_val = A[j] + diff              # next value
#                     if next_val not in mapping.keys():  # 查找 next_val 是否在 j 之后的索引对应的列表中
#                         break
#                     for_tag = False                     # 标示 是否在mapping[next_val]的索引列表中找到index>j: true 找到
#                     for index in mapping[next_val]:     # 在列表中，则遍历mapping，找到大于j的索引，更新j为该索引
#                         if index > j:
#                             j = index                   # 更新索引后退出该层循环，继续 while loop
#                             length += 1
#                             max_length = max(max_length, length)
#                             for_tag = True
#                             break
#                     if not for_tag:                     # 找到index>j，继续 while loop,否则退出while
#                         flag = False
#         return max_length
