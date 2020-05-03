# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-04-15 10:39:28
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-15 12:35:25

''' 01矩阵
给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
两个相邻元素间的距离为 1 。
示例 1:
输入:
    0 0 0
    0 1 0
    1 1 1
输出:
    0 0 0
    0 1 0
    1 2 1
思路： 多源bfs 或 dp
dp: dp略微麻烦，特别是要注意边界问题
'''

from collections import deque


class Solution:
    def updateMatrix_bfs(self, matrix):
        if not matrix:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        # 方向数组 down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isCrossBorder(x, y):
            ''' 索引是否越界: 越界：True, 没越界：False '''
            return not (0 <= x < rows and 0 <= y < cols)

        dequeue = deque()
        # 1. 找出所有的 start point (matrix中值为0的点)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dequeue.append((i, j))
                else:
                    matrix[i][j] = -1
        depth = 0
        while dequeue:
            # 逐层遍历，每一层遍历之后 depth+1  -----> 可以知道当前bfs了多少层
            for _ in range(len(dequeue)):
                i, j = dequeue.popleft()
                for di, dj in directions:
                    ti = i + di
                    tj = j + dj
                    if not isCrossBorder(ti, tj) and matrix[ti][tj] < 0:
                        dequeue.append((ti, tj))
                        matrix[ti][tj] = depth + 1
            depth += 1
        return matrix

    def updateMatrix_bfs_2(self, matrix):           # 不记录bfs了多少层，增加visited集合
        if not matrix:
            return matrix
        rows, cols = len(matrix), len(matrix[0])
        # 方向数组 down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isCrossBorder(x, y):
            ''' 索引是否越界: 越界：True, 没越界：False '''
            return not (0 <= x < rows and 0 <= y < cols)

        dequeue = deque()
        visited = set()
        # 1. 找出所有的 start point (matrix中值为0的点)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dequeue.append((i, j))
                    visited.add((i, j))
        # 将所有相邻节点加入队列
        while dequeue:
            i, j = dequeue.popleft()
            for di, dj in directions:
                ti = i + di
                tj = j + dj
                if not isCrossBorder(ti, tj) and (ti, tj) not in visited:
                    dequeue.append((ti, tj))
                    visited.add((ti, tj))
                    matrix[ti][tj] = matrix[i][j] + 1
        return matrix

    def updateMatrix_dp(self, matrix):
        if not matrix:
            return matrix
        rows = len(matrix)
        cols = len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dp = [[10**9] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dp[i][j] = 0

        # 只有 水平向左移动 和 竖直向上移动，需正向遍历，当前值与左边和上面的值有关，注意动态规划的计算顺序
        for i in range(rows):
            for j in range(cols):
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        # 只有 水平向右移动 和 竖直向下移动，需反向遍历，注意动态规划的计算顺序
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i + 1 < rows:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < cols:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp


if __name__ == '__main__':
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = Solution().updateMatrix_bfs_2(matrix)
    print(res)
