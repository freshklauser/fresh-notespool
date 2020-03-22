# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-22 16:01:29
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-22 17:02:15

'''[945. 使数组唯一的最小增量]
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
返回使 A 中的每个值都是唯一的最少操作次数。
示例 1:
    输入：[1,2,2]
    输出：1
    解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

思路：
    动态规划 dp[i]:A[:i]的每个值唯一的最少操作次数
    判断A[i]是否在A[:i]中出现过
        出现过：dp[i] = dp[i-1] + 1
        没出现：dp[i] = dp[i-1]
'''


class Solution1:
    ''' 暴力法：54 / 59 个通过测试用例: 超时'''

    def minIncrementForUnique(self, A):
        if not A:
            return 0
        n = len(A)
        # 构建dp
        dp = [0] * n
        dp[0] = 0
        for i in range(1, n):
            flag = True
            inc = 0
            if A[i] not in A[:i]:
                dp[i] = dp[i - 1]
            else:
                while flag:
                    A[i] += 1
                    inc += 1
                    dp[i] = dp[i - 1] + inc
                    if A[i] not in A[:i]:
                        flag = False
        return dp[-1]


class Solution:
    ''' 贪心算法：排序，判断A[i] <= A[i-1]则operate = A[i-1] - A[i] + 1, 同时更新operate次inc操作后的A[i]的值'''

    def minIncrementForUnique(self, A):
        A = sorted(A)           # or A.sort() --> 原地更改， sorted(A)-->非原地更改
        operate = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                operate += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return operate


if __name__ == '__main__':
    # A = [3, 2, 1, 2, 1, 7]
    # A = [1, 2, 2, 4]
    A = [3, 2, 1, 2, 1, 7]
    res = Solution().minIncrementForUnique(A)
    print(res)
