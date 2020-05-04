# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 10:11:59
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-10 10:45:08

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

     交易次数不限：k--> float("inf"), k-1-->float("inf")  ==>  k = k-1
                 i-1:无股票，i不操作  ； i-1:持股，则i卖出 (buy时才记录操作，卖时不记录)
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])

                    i-1:有股，i不操作; i-1:无股，则i买入, 利润-当前价，记录k(当天为k，则前一天次数为k-1)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
"""


class Solution:
    def maxProfit(self, prices):
        if prices == []:
            return 0

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        # 初始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]    # 第0填持有，必然是该填买入

        # 状态转移关系
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [1, 2, 3, 4, 5]
    prices = [7, 6, 4, 3, 1]
    res = Solution().maxProfit(prices)
    print(res)
