# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-29 12:01:53
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-29 16:27:38

'''地图分析：bfs
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，
你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

思路：bfs
    1）bfs搜索确定所有的陆地（start_points）
    2）同时遍历陆地，记录每一个陆地到对应的最远海洋的距离，返回所有距离中的最大值

'''

from collections import deque


class Solution:

    # @staticmethod     # self代表类的实例，使用staticmethod时，def参数中不需要使用self,即不需要实例化
    def maxDistance(self, grid):
        rows, cols = len(grid), len(grid[0])
        # 方向数组 down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isCrossBorder(x, y):
            ''' 索引是否越界: 越界：True, 没越界：False '''
            return not (0 <= x < rows and 0 <= y < cols)

        # 1. 确定搜索列表(起点列表) -- 所有陆地
        dequeue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dequeue.append((i, j))

        # 2. 没有陆地或者没有海洋，返回-1
        if len(dequeue) == rows * cols or len(dequeue) == 0:
            return -1

        # 3. bfs -- 直到搜索完所有海洋，dequeue为空
        # searched = set() # 这里不用searched，直接原址修改searched的cell的值为距离
        depth = -1                                  # 起点遍历完才开始depth从1累加深度
        while dequeue:
            # 逐层遍历，每一层遍历之后 depth+1
            for _ in range(len(dequeue)):
                i, j = dequeue.popleft()
                # searched.add((i, j))
                # 四周的cell没越界并且是海洋，则添加到dequeue中
                for di, dj in directions:
                    ti = i + di
                    tj = j + dj
                    if not isCrossBorder(ti, tj) and grid[ti][tj] == 0:
                        dequeue.append((ti, tj))
                        grid[ti][tj] = 1            # 访问过的海洋标记为陆地，也可以其他标记，或者直接赋值为搜索深度(这样就不用单独维护depth）
            # 一层遍历完之后，depth+1, 然后继续遍历下一层
            depth += 1
        return depth


class Solution1:
    ''' 起点列表使用 列表解析，队列使用列表 '''

    # @staticmethod     # self代表类的实例，使用staticmethod时，def参数中不需要使用self,即不需要实例化
    def maxDistance(self, grid):
        rows, cols = len(grid), len(grid[0])
        # 方向数组 down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isCrossBorder(x, y):
            ''' 索引是否越界: 越界：True, 没越界：False '''
            return not (0 <= x < rows and 0 <= y < cols)

        # 1. 确定搜索列表(起点列表) -- 所有陆地
        dequeue = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == 1]
        island_num = len(dequeue)

        # 2. 没有陆地或者没有海洋，返回-1
        if island_num == rows * cols or island_num == 0:
            return -1

        # 3. bfs -- 直到搜索完所有海洋，dequeue为空
        # searched = set() # 这里不用searched，直接原址修改searched的cell的值为距离
        depth = -1                                  # 起点遍历完才开始depth从1累加深度
        while dequeue:
            # 逐层遍历，每一层遍历之后 depth+1
            for _ in range(len(dequeue)):
                i, j = dequeue.pop(0)
                # searched.add((i, j))
                # 四周的cell没越界并且是海洋，则添加到dequeue中
                for di, dj in directions:
                    ti = i + di
                    tj = j + dj
                    if not isCrossBorder(ti, tj) and grid[ti][tj] == 0:
                        dequeue.append((ti, tj))
                        grid[ti][tj] = 1            # 访问过的海洋标记为陆地，也可以其他标记，或者直接赋值为搜索深度(这样就不用单独维护depth）
            # 一层遍历完之后，depth+1, 然后继续遍历下一层
            depth += 1
        return depth


if __name__ == '__main__':
    grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    res = Solution().maxDistance(grid)
    print(res)
