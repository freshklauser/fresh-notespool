# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-21 11:30:33
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-28 11:01:33

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
        visited = set()
        i = 1
        while stack:
            remain_x, remain_y = stack.pop()
            # 出口
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                print("Success: remain_x={}, remain_y={}, z={}".format(remain_x, remain_y, z))
                return True
            # 判断stack中取出的元素是否visited
            if (remain_x, remain_y) in visited:
                continue
            # 不在visited则先添加到visited中，然后执行dfs
            visited.add((remain_x, remain_y))

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
            print("i-->", i, visited)
            print("    ", stack)
            i += 1
        return False


class Solution1:
    ''' BFS '''

    def canMeasureWater(self, x, y, z):
        'stack --> queue, 改变pop的位置，其他不变'
        queue = [(0, 0)]
        visited = set()
        i = 1
        while queue:
            'TODO: dfs从栈顶取元素即pop(), bfs从队列首取元素即pop(0)'
            remain_x, remain_y = queue.pop(0)
            # 出口
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                print("Success: remain_x={}, remain_y={}, z={}".format(remain_x, remain_y, z))
                return True
            # 判断queue中取出的元素是否visited
            if (remain_x, remain_y) in visited:
                continue
            # 不在visited则先添加到visited中，然后执行dfs
            visited.add((remain_x, remain_y))

            # DFS深度搜索 添加元素至queue
            '把 X 壶倒空'
            queue.append((0, remain_y))
            '把 Y 壶倒空'
            queue.append((remain_x, 0))
            '把 X 壶灌满'
            queue.append((x, remain_y))
            '把 Y 壶灌满'
            queue.append((remain_x, y))
            '把 X 壶的水灌进 Y 壶，直至灌满或倒空'
            queue.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            '把 Y 壶的水灌进 X 壶，直至灌满或倒空'
            queue.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
            print("i-->", i, visited)
            print("    ", queue)
            i += 1
        return False


class Solution2:
    ''' 贝柤定理：最大公约数 '''

    def canMeasureWater(self, x, y, z):
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return x + y == z or z == 0
        import math
        # 最大公约数公式
        greatest_common_divisor = math.gcd(x, y)
        # print(greatest_common_divisor)
        return z % greatest_common_divisor == 0


if __name__ == '__main__':
    x, y, z = 7, 5, 4
    # x, y, z = 2, 6, 16
    res = Solution2().canMeasureWater(x, y, z)
    print(res)
