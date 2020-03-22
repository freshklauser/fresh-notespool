# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-11 22:07:09
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-14 19:44:05

'''
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，
每步可以删除任意一个字符串中的一个字符。
示例 1:
    输入: "sea", "eat"
    输出: 2
    解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
'''

import numpy as np

class Solution:
    def minDistance(self, word1, word2):
        # 可以转化为最长公共子序列问题，return m+n-2*len(substring)
        row = len(word1)
        col = len(word2)
        max_length = 0
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        max_length = dp[row][col]
        print(np.array(dp))
        return row + col - 2 * max_length


if __name__ == '__main__':
    word1 = "seaiuyo"
    word2 = "eae"
    res = Solution().minDistance(word1, word2)
    print(res)
