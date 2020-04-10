# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-04-08 08:41:00
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-04-08 10:15:08

'''{机器人的运动范围}
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
    输入：m = 2, n = 3, k = 1
    输出：3

思路：dfs 或 bfs
    dfs：迭代
'''

from functools import reduce

class Solution:
    def movingCount(self, m, n, k):

        cnt = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        searched = set()

        def isValid(x, y):
            return 0 <= x < m  and 0 <= y < n

        def sum_xy(a, b):
            return reduce(lambda x,y: x + y, divmod(a, 10)) + reduce(lambda x,y: x + y, divmod(b, 10))

        def dfs(i, j):
            for x, y in directions:
                ti = i + x
                tj = j + y
                if isValid(ti, tj) and sum_xy(ti, tj) <= k and (ti, tj) not in searched:
                    searched.add((ti, tj))      # 符合条件的点加入searched，再dfs
                    dfs(ti, tj)
        # start dfs
        searched.add((0, 0))                    # 起点先加入searched，再dfs
        dfs(0, 0)
        # print(searched)
        return len(searched)


if __name__ == '__main__':
    m, n, k = 5, 4, 0
    res = Solution().movingCount(m, n, k)
    print(res)