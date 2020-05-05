# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-05 17:13:22
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 23:02:40

"""
题目：
    第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。
    每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
    返回载到每一个人所需的最小船数。(保证每个人都能被船载)。

思路：
    贪心算法/贪婪算法 ( 每次都找局部最优解，最终得到的就是全局最优解 )

双指针+有序列表，head tail <---> 最轻 最重
如果最重的人无法与任何人配对，那么他们将自己独自乘一艘船
"""


class Solution:
    def numRescueBoats(self, people, limit):
        'step-1: 列表排序 --> 有序列表'
        people = sorted(people, reverse=False)
        num = 0
        head = 0
        tail = len(people) - 1
        while head <= tail:
            if head == tail:
                num += 1
                break
            num += 1
            '最轻 + 最重'
            if people[head] + people[tail] <= limit:
                head += 1
            tail -= 1
        return num


if __name__ == '__main__':
    people = [3, 5, 3, 4]
    limit = 5
    res = Solution().numRescueBoats(people, limit)
    print(res)
