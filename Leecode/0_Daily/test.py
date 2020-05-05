# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-04-05 14:25:12
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-05 14:45:02
import numpy

class Solution:

    # 深度优先算法 '''
    def numIslands(self, grid):
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        if row == 0:
            return 0
        if col == 0:
            return 0

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))    # 上，下，左，右
        count = 0                                          # record number of island
        island = set()

        def dfs(i, j):
            '''(i,j) 满足的条件： A[i][j] == 1,(i,j)不在islands中'''
            island.add((i, j))                             # grid[i][j]添加到islands中
            grid[i][j] = -1                                # grid[i][j]标记后置-1,避免再次判断1
            for x, y in directions:
                ti = i + x
                tj = j + y
                if 0 <= ti < row and 0 <= tj < col and (ti, tj) not in island and grid[ti][tj] == 1:
                    dfs(ti, tj)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:                         # start point
                    dfs(i, j)                               # 执行dfs算法
                    count += 1
        # print(islands_map)`
        return count


if __name__ == '__main__':
    grid = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    res = Solution().numIslands(grid)
    print(res)
    arr = numpy.array([1, 2, 3])
