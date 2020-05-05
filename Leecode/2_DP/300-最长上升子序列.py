# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 16:50:24
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-11 19:24:09

"""{description}
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)

        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        res = max(dp)
        return res


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    res = Solution().lengthOfLIS(nums)
    print(res)
