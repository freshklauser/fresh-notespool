# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 10:48:50
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-10 13:56:00

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

k <= 2  [0,1,2]：
dp[i][k][0]: 第i天空仓、最多操作k次交易的最大利润
dp[i][k][1]: 第i天持仓、最多操作k次交易的最大利润
target: dp[n-1][2][0]

状态转义关系：                    # i空仓：i-1持仓,i卖出(i卖出不记录交易，则i-1持仓的最多交易次数为k)
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                                  # i持仓：i-1空仓，i买入(买入记录交易一次,则i-1空仓的最多交易次数为k-1)
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
'''


class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        n = len(prices)
        K = 2
        # 定义dp数组
        dp = [[[0, 0] for _ in range(3)] for _ in range(n)]
        # 状态转移关系
        for i in range(0, n):
            for k in range(1, K + 1):
                if i == 0:
                    # 处理 base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[0]
                else:
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][K][0]


if __name__ == '__main__':
    # prices = [7, 6, 4, 3, 1]
    # prices = [3, 3, 5, 0, 0, 3, 1, 4]
    # prices = [1, 2, 3, 4, 5]
    prices = [3, 2, 6, 5, 0, 3]
    res = Solution().maxProfit(prices)
    print(res)
