# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-25 09:09:19
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-28 11:01:23

'''{description}
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：
    输入：[[2]]
    输出：10
示例 2：
    输入：[[1,2],[3,4]]
    输出：34

思路：
    看到題目就不想做，直接复制了官方解题和评论区的代码
'''


class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans


class Solution1(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sm = 0
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n > 0:
                    sm += 4 * n + 2
                    if i > 0 and grid[i - 1][j] > 0:
                        t = grid[i - 1][j] if grid[i - 1][j] < n else n
                        sm -= t << 1
                    if j > 0 and grid[i][j - 1] > 0:
                        t = grid[i][j - 1] if grid[i][j - 1] < n else n
                        sm -= t << 1
        return sm


if __name__ == '__main__':
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    res = Solution().surfaceArea(grid)
    print(res)
