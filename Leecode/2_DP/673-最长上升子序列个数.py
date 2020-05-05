# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 17:01:21
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-11 22:06:21

"""{description}
思路：
    构建两个一维dp，分别存储 i处结尾的最长子序列长度 和 i处结尾的最长子序列个数
"""


class Solution:
    def findNumberOfLIS(self, nums):
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n                # 代表i结尾的最长子序列长度
        counter = [1] * n           # 代表i结尾的最长子序列个数
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:       # 第一次找到以nums[i]结尾的最长子序列
                        dp[i] = max(dp[i], dp[j] + 1)
                        counter[i] = counter[j]
                    elif dp[j] + 1 == dp[i]:    # 第n次找到 n>1
                        counter[i] += counter[j]
        # 遍历:获取最大长度的counter之和
        res = 0
        for i in range(n):
            if dp[i] == max(dp):
                res += counter[i]
        return res


if __name__ == '__main__':
    nums = [1, 3, 5, 4, 7, 2, 3, 6, 8]
    # nums = [2, 2, 2, 2, 2]
    res = Solution().findNumberOfLIS(nums)
    print(res)
