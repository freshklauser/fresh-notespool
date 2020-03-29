# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 15:44:08
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 15:09:32

'''{description}
子序列问题解题模板
'''

'1、第一种思路模板是一个一维的 dp 数组：'
n = len(arr)
np = [0] * n    # 有时需要初始化为1
for i in range(n):
    for j in range(i):
        'if case or not'
        dp[i] = max(dp[i], dp[j] + <int > )
        'or dp[i] = min(dp[i], dp[j] + <int>)'


'2、第二种思路模板是一个二维的 dp 数组：'
--> 经常是从后往前遍历
int n = arr.length
int[][] dp = new dp[n][n]

for (int i=0
     i < n
     i + +) {
    for (int j=0
         j < n
         j + +) {
        if (arr[i] == arr[j])
        dp[i][j] = dp[i][j] + ...
        else
        dp[i][j] = 最值(...)
    }
}

    2.1 涉及两个字符串 / 数组时（比如最长公共子序列），dp 数组的含义如下：
    在子数组 arr1[0..i] 和子数组 arr2[0..j] 中，我们要求的子序列（最长公共子序列）长度为 dp[i][j]。

    2.2 只涉及一个字符串 / 数组时（比如本文要讲的最长回文子序列），dp 数组的含义如下：
    在子数组 array[i..j] 中，我们要求的子序列（最长回文子序列）的长度为 dp[i][j]。
