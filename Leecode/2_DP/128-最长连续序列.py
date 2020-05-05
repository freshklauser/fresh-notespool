# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-11 22:02:43
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-07 22:43:57

"""
给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。
示例:
    输入: [100, 4, 200, 1, 3, 2]
    输出: 4
    解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
思路：
    排序 + 一维dp (从前往向遍历)
"""


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = sorted(nums)
        n = len(nums)
        dp = [1] * n        # 以 nums[i]为结尾元素的最长连续序列长度

        for i in range(n - 1):
            if nums[i + 1] == nums[i]:
                dp[i + 1] = dp[i]
            elif nums[i + 1] == nums[i] + 1:
                dp[i + 1] = dp[i] + 1
            else:
                dp[i + 1] = 1
        # print(dp)
        return max(dp)

    def __str__(self):
        return "Longest Consecutive"


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 100, 200, 200, 201, 199, 198, 202, 200]
    res = Solution().longestConsecutive(nums)
    print(res)
    s = Solution()
    print(s)
    # print(s.__dict__)
    # print(s.__str__())
