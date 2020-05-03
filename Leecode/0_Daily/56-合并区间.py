# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-04-16 11:56:31
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-16 12:09:56


class Solution:
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals

        intervals_sorted = sorted(intervals, key=lambda x: x[0], reverse=False)
        # print(intervals_sorted)

        res = []
        length = len(intervals_sorted)
        left = intervals_sorted[0][0]
        right = intervals_sorted[0][1]

        for i in range(1, length):
            cursor = intervals_sorted[i]
            if cursor[0] > right:
                res.append([left, right])
                # 更新left和right
                left = cursor[0]
                right = cursor[1]
            else:
                right = max(right, cursor[1])
            if i == length - 1:
                res.append([left, right])

        return res


if __name__ == '__main__':
    intervals = [[11, 16], [2, 6], [8, 10], [15, 18]]
    res = Solution().merge(intervals)
    print(res)
