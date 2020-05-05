# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 09:27:30
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-10 10:11:42

"""
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
              max(   选择 rest  ,           选择 sell      )
解释：今天我没有持有股票，有两种可能：
要么是我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
要么是我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
              max(   选择 rest  ,           选择 buy         )
解释：今天我持有着股票，有两种可能：
要么我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；
要么我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。

题目1：
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
"""


class Solution:
    ''' 非dp '''

    def maxProfit(self, prices):
        temp = max_profit = 0
        for i in range(len(prices) - 1):
            temp = max(0, prices[i + 1] - prices[i] + temp)
            max_profit = max(max_profit, temp)
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    res = Solution().maxProfit(prices)
    print(res)
