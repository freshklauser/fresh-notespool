# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-05-03 20:43:04
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-03 21:12:41

''' 最大连续子序和
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.
   asdf
Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6.

思路： 动态规划
    dp[i] = max(dp[i - 1] + v, v)   (不管v正还是v负)

    -- dp[i]: 数组 nums 中以 num[i] 结尾的最大连续子序和
'''

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [0] * n
        for i, v in enumerate(nums):
            dp[i] = max(dp[i - 1] + v, v)
        return max(dp)


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = Solution().maxSubArray(nums)
    print(res)
    print(res)
