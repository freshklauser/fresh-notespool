# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 16:01:42
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 15:42:11

"""{description}
二维dp[i][j]: 以i开始 以j结尾的回文子序列长度
状态转移:
如果 arr[i] == arr[j], dp[i][j] = dp[i+1][j-1] + 2
如果 arr[i] != arr[j], dp[i][j] = max(dp[i][j-1], dp[i+1][j])
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not str:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # base case  i==j时子串长度为1，则dp[i][j] = 1
        for i in range(n):
            dp[i][i] = 1

        # 状态转移关系 i 反向遍历n->-1， j正向遍历i->n
        # 遍历顺序，i 从最后一个字符开始往前遍历，j 从 i + 1 开始往后遍历，这样可以保证每个子问题都已经算好了
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # base case
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2

        return dp[0][n - 1]


if __name__ == '__main__':
    s = "bbbab"
    res = Solution().longestPalindromeSubseq(s)
    print(res)
