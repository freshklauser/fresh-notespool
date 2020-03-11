# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 17:01:21
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-11 17:25:37

'''{description}

'''

class Solution:
    def findNumberOfLIS(self, nums):
        if not nums: return 0

        n = len(nums)
        dp = [1] * n
        max_num = 0
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        max_len = max(dp)
        res = dp.count
