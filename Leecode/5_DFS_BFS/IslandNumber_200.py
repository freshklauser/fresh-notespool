# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-01 13:55:02
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-04-08 10:21:22

""" 岛屿数量
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，
并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:
    输入:
    11110
    11010
    11000
    00000

    输出: 1

思路：
    dfs(迭代)
    bfs(遍历)
"""


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
        # islands_map = {}

        def dfs(i, j):
            '''(i,j) 满足的条件： A[i][j] == 1,(i,j)不在islands中'''
            island.add((i, j))                             # grid[i][j]添加到islands中
            grid[i][j] = -1                                # grid[i][j]标记后置-1,避免再次判断1
            for x, y in directions:
                ti = i + x
                tj = j + y
                if 0 <= ti < row and 0 <= tj < col and (ti, tj) not in island and grid[ti][tj] == "1":
                    dfs(ti, tj)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":                       # start point
                    dfs(i, j)                               # 执行dfs算法
                    count += 1
                    # islands_map[count] = island           # 保存每个island的元素
                    # island = set()                        # 查找完一个island后置空
                    # print("island: ", islands_map[count])
                    # print("island element` number: ", len(islands_map[count]))
                    # print("islands number in total: ", count)
                    # print('--------------------------------------------------------')
        # print(islands_map)`
        return count

    # 广度优先算法
    def numIslands_1(self, grid):
        if grid == []:
            return 0
        row = len(grid)
        col = len(grid[0])
        if row == 0:
            return 0
        if col == 0:
            return 0

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        island_num = 0
        # searched = set()
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":       # 每一个island的起点
                    island_num += 1         # 找到起点后island_num增加1
                    grid[i][j] = -1         # 将改点置为-1,表示访问过
                    queue.append((i, j))    # 该起点加入到queue中
                    # 开始bfs搜索
                    while queue:
                        ci, cj = queue.pop(0)               # 逐个pop出queue中的元素，判断邻居是否有"1"
                        for x, y in directions:
                            ti = ci + x
                            tj = cj + y
                            if 0 <= ti < row and 0 <= tj < col and (ti, tj) not in queue and grid[ti][tj] == "1":
                                grid[ti][tj] = -1           # 置为-1,表示访问过
                                queue.append((ti, tj))       # 邻居中有"1"的加入到queue中
        # print('island_num: ', island_num)
        return island_num


if __name__ == '__main__':
    A = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    # A = [["1", "1", "0", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "1"], ["0", "0", "1", "0", "0"]] * 100

    # A = [[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]]
    output = Solution().numIslands(A)
    print(output)
