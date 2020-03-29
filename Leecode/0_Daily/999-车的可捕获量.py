# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-26 19:13:44
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-26 19:45:22


class Solution:
    def numRookCaptures(self, board):
        num = 0
        cx, cy = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    cx, cy = i, j

        dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
        for i in range(4):      # 4个方向
            step = 1
            while True:
                # 朝一个方向移动
                mx = cx + step * dx[i]
                my = cy + step * dy[i]
                if mx < 0 or mx >= 8 or my < 0 or my >= 8 or board[mx][my] == "B":
                    break
                if board[mx][my] == "p":
                    num += 1
                    break
                step += 1
        return num


if __name__ == '__main__':
    board = [[".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             ["p", "p", ".", "R", ".", "p", "B", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", "B", ".", ".", ".", "."],
             [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."]]
    print(board[3][5])
    res = Solution().numRookCaptures(board)
    print(res)
