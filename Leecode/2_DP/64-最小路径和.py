# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-09 09:12:16
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 15:42:19

"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
    输入:
        [
          [1,3,1],
          [1,5,1],
          [4,2,1]
        ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid):
        if grid == [] or grid == [[]]:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        # 第0行
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # 第0列
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = Solution().minPathSum(grid)
    print(res)
