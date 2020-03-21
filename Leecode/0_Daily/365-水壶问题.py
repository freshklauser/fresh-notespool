# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-21 11:30:33
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-21 12:29:39

'''{水壶问题}
dfs
    把 X 壶的水灌进 Y 壶，直至灌满或倒空；
    把 Y 壶的水灌进 X 壶，直至灌满或倒空；
    把 X 壶灌满；
    把 Y 壶灌满；
    把 X 壶倒空；
    把 Y 壶倒空。

TIPS:
如果某天你写了一个BFS版本的搜索，如何最快的速度再写一份DFS版本发的呢？只需要把queue改为stack就可以了~
还有，visited这个set的更新，一定要在入queue的时候，而不是在queue取出元素的时候，否则队列里会塞很多很多已经遍历过的状态
'''


class Solution:
    ''' DFS '''
    def canMeasureWater(self, x, y, z):
        stack = [(0, 0)]
        visited =set()
        while True:
            remain_x, remain_y = stack.pop()
            # 出口
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            # 判断stack中取出的元素是否visited
            if (remain_x, remain_y) in visited:
                continue

            # DFS深度搜索 添加元素至stack
            '把 X 壶倒空'
            stack.append((0, remain_y))
            '把 Y 壶倒空'
            stack.append((remain_x, 0))
            '把 X 壶灌满'
            stack.append((x, remain_y))
            '把 Y 壶灌满'
            stack.append((remain_x, y))
            '把 X 壶的水灌进 Y 壶，直至灌满或倒空'
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            '把 Y 壶的水灌进 X 壶，直至灌满或倒空'
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
            print(stack)
            break
        return False


if __name__ == '__main__':
    x, y, z = 3, 5, 4
    res = Solution().canMeasureWater(x, y, z)
    print(res)
