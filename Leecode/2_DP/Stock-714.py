# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 15:35:57
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-14 19:59:46

"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
    解释: 能够达到的最大利润:
    在此处买入 prices[0] = 1
    在此处卖出 prices[3] = 8
    在此处买入 prices[4] = 4
    在此处卖出 prices[5] = 9
    总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
思路：
在买入时将fee作为成本即可 （也可在卖出时减去fee）
"""


class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n <= 1:
            return 0

        dp = [[0, 0] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -(prices[0] + fee)
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - (prices[i] + fee))

        return dp[n - 1][0]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    res = Solution().maxProfit(prices, fee)
    print(res)
