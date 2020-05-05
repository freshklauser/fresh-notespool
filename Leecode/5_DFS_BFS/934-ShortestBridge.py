# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-27 20:21:56
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-05 10:58:07

import time


class Solution:
    def shortestBridge(self, A):
        row, col, island = len(A), len(A[0]), set()

        def dfs(i, j):
            # 判断neighbors是否在island中(val==1)，注意边界点,一次遍历4个neighbors
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):     # (up, down, left, right)
                ti = i + x
                tj = j + y
                if 0 <= ti < row and 0 <= tj < col and A[ti][tj] == 1 and (ti, tj) not in island:
                    island.add((ti, tj))     # 边界范围内，val==1 且 neighbor 不在island中(避免重复dfs)
                    dfs(ti, tj)
                    time.sleep(1)
        # --> start point search: 遍历确定第一个值为1的点，需要注意break的正确方式
        flag = 0
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    island.add((i, j))       # start point added to island
                    dfs(i, j)
                    flag = 1
                    break
            if flag == 1:
                break
        # searched = set()
        queue = list(island)
        bridge_length = 0
        while queue:
            numbers = len(queue)
            for ind in range(numbers):      # # 以每一维关系的列表长度决定for循环的层次和bridge_length
                i, j = queue.pop(0)
                # searched.add((i,j))
                # print(queue, '<---->', searched)
                for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):   # 将queue的一维朋友中的val==0添加到队列中
                    ti = i + x
                    tj = j + y
                    if 0 <= ti < row and 0 <= tj < col:
                        if A[ti][tj] == 1 and (ti, tj) not in island:
                            return bridge_length
                        elif A[ti][tj] == 0:
                            A[ti][tj] = -1
                            queue.append((ti, tj))
            bridge_length += 1
        return bridge_length


if __name__ == '__main__':
    # A = [[0,1,1,0], [1,1,0,0], [1,0,0,1]]
    A = [[0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0]] * 20
    # print(len(A))
    output = Solution().shortestBridge(A)
    print()
    print(output)
