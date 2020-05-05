# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 14:40:40
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-10 15:34:36

"""
题目：
    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:
    输入: [1,2,3,0,2]
    输出: 3
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

思路：
k次：k --> inf (可简化三维dp为二维dp)
target: dp[n-1][0]
简化后状态转换关系：
               i-1空仓,选择rest，  i-1持仓，i选择sell
dp[i][0] = max(dp[i-1][0],         dp[i-1][1] + prices[i])
               i-1持仓，选择rest， i-2空仓，i选择buy
dp[i][1] = max(dp[i-1][1],         dp[i-2][0] - prices[i])
"""


class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0

        dp = [[0, 0] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = 0
        dp[1][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])  # 后者：i-2空仓,i选择buy
        return dp[len(prices) - 1][0]


if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    res = Solution().maxProfit(prices)
    print(res)
