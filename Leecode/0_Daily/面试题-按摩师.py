# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-25 09:03:24
# @Last Modified by:   klaus
# @Last Modified time: 2020-03-25 09:04:08

'''{description}
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，
替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

示例 1：
    输入： [1,2,3,1]
    输出： 4
    解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
'''

class Solution:
    def massage(self, nums):
        # 动态规划问题 选 or 不选
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums), 1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[len(nums) - 1]