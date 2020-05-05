# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-26 19:33:50
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 22:55:38

"""
最大正方形面积：动态规划问题 dp
"""


class Solution:
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        res = 0
        for i in range(row):
            for j in range(col):
                matrix[i][j] = 1 if matrix[i][j] == '1' else 0
                if i == 0 or j == 0:
                    res = max(matrix[i][j], res)
                elif matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                    res = max(matrix[i][j], res)
        return res * res


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    squres = Solution().maximalSquare(matrix)
    print(squres)
