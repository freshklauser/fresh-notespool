# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-17 15:45:59
# @Last Modified by:   Administrator
# @Last Modified time: 2020-04-16 11:55:38

'''{合并区间}
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
    输入: [[1,3],[2,6],[8,10],[15,18]]
    输出: [[1,6],[8,10],[15,18]]
    解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
思路：
    1. [left, right]按left升序排列，比对right，如果cur_right>=next_left, right=max(cur_right, next_right)
'''


class Solution:
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals
        # 'intervals 按照 left 排序'
        intervals_sorted = sorted(intervals, key=lambda x: x[0], reverse=False)
        # print(intervals_sorted)
        res = []
        length = len(intervals_sorted)
        left = intervals_sorted[0][0]
        right = intervals_sorted[0][1]

        for i in range(1, length):
            # i 从1开始的话需要单独讨论length=1的情况
            cur_interval = intervals_sorted[i]
            if right >= cur_interval[0]:
                right = max(right, cur_interval[1])
            else:
                res.append([left, right])
                # 更新 left 和 right
                left = cur_interval[0]
                right = cur_interval[1]
            if i == length - 1:
                # 添加当前的 left,right --> 全部都重叠的要特别注意
                res.append([left, right])
        return res


if __name__ == '__main__':
    # intervals = [[1,3],[2,6],[8,10],[15,18], [5, 9]]
    intervals = [[1, 4], [4, 5]]
    res = Solution().merge(intervals)
    print(res)
