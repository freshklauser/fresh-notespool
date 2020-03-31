# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-10 15:53:28
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-31 14:39:23

'''{description}
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
    插入一个字符
    删除一个字符
    替换一个字符
示例 1:
    输入: word1 = "horse", word2 = "ros"
    输出: 3
    解释:
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
思路：
dp[i][j]: word1的前i个字符与word2的前j个字符之间的最短编辑距离
相同：dp[i][j] = dp[i-1][j-1]
不同，则转换关系：
1) 插入：dp[i][j] = dp[i][j-1] + 1     # word1前i个字符与word2前(j-1)个字符的编辑距离+1
2) 删除：dp[i][j] = dp[i-1][j] + 1
3) 替换: dp[i][j] = dp[i-1][j-1] + 1
- 第一个单词的前i位变成第二个单词的前j-1位，然后再插入一个字符（d[i][j-1]+1）
- 第一个单词的前i-1位变成第二个单词的前j位，然后再删去一个字符（d[i-1][j]+1）
- 第一个单词的前i-1位变成第二个单词的前j-1位，然后替换最后一个字符，如果最后一个字符相同，
  即第一个单词的第i位和第二个单词的第j位相同的话，就不用替换了（d[i-1][j-1]），
  反之，如果不同就替换最后一位（d[i-1][j-1]+1）
dp[i-1][j-1]  dp[i-1][j]  <---->  替换/跳过  删除
dp[i][j-1]    dp[i][j]    <---->     插入'''
class Solution:
    def minDistance(self, word1, word2):
        row = len(word1)
        col = len(word2)
        if row * col == 0:
            return row + col
        # 考虑到位空的情况，需添加第0行第0列代表为空，这样第i个字符才是word1[i-1]
        # dp[i][j]: word1的前i个字符word1[:i]与word2的前j个字符word2[:j]之间的最短编辑距离
        dp = [[0] * (col + 1) for _ in range(row + 1)]
        # base case
        for i in range(row + 1):
            dp[i][0] = i
        for j in range(col + 1):
            dp[0][j] = j
        # 二维表格边界：即0行和0列
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                down = dp[i][j - 1] + 1
                left = dp[i - 1][j] + 1
                left_down = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:  # 第 i 个字符对应下标不是 i-1
                    left_down += 1
                dp[i][j] = min(down, left, left_down)
        return dp, dp[row][col]


if __name__ == '__main__':
    word1 = "the"
    word2 = "than"
    dp, res = Solution().minDistance(word1, word2)
    print(res)
    # print(dp)
