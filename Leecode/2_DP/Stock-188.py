# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 11:08:33
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-14 19:58:53

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
k次：  target: dp[n-1][k][0]
状态转移关系：
                                  # i空仓：i-1持仓,i卖出(i卖出不记录交易，则i-1持仓的最多交易次数为k)
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                                  # i持仓：i-1空仓，i买入(买入记录交易一次,则i-1空仓的最多交易次数为k-1)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])"""


class Solution:
    """ 针对Solution1的优化：主要优化k, 最大购买次数与len(prices)有关，不能当天买和卖
    当k特别大时，k-1与k基本相同，可以直接使用k不做限制情况下的方法，三维简化为二维
    """

    def maxProfit_k_inf(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[n - 1][0]

    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1:
            return 0
        if k >= n // 2:  # 针对k的限制, 当k >= n//2时，直接调用k不做限制情况下的二维dp方法
            return self.maxProfit_k_inf(prices)
        # 构建dp 注意 k+1, 不是k
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        # 状态转移关系
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:          # 初始状态
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]


class Solution1:
    """ 当k很大时，该方法空间复杂度过大，leecode超出内存 """

    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1:
            return 0
        # 构建dp 注意 k+1, 不是k
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        # 状态转移关系
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:          # 初始状态
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]


if __name__ == '__main__':
    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    res = Solution().maxProfit(k, prices)
    print(res)
