# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-27 13:41:54
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-13 20:54:08

'''最简单方法：'''


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        for length in range(len(s), 0, -1):     # 子串长度
            for i in range(0, len(s) - length + 1):   # start index, 遍历给定长度的所有子串
                now_s = s[i:i + length]
                if now_s == now_s[::-1]:        # 子串与其逆序相同，则为结果
                    return now_s


class Solution(object):
    def longestPalindrome(self, s):
        """type s: str"""
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1, n):
            even = s[i - max_len:i + 1]     # 偶数长度子串 even+2-->even
            odd = s[i - max_len - 1:i + 1]    # 奇数长度子串 odd +1-->odd
            # 重点：判断子串与逆序相等后的start和len更新(end一直都是i+1)
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]


# class Solution2:                # 与1一样
#     def longestPalindrome(self, s):
#         windows_size = len(s)
#         while windows_size > 0:
#             for i in range(len(s)-windows_size+1):
#                 tmp = s[i:i+windows_size]
#                 if tmp == tmp[::-1]:
#                     return tmp
#             windows_size -= 1
#         return s


# 动态规划算法: 先找最长公共子串（自徐磊区别，不同时 dp[i][j]=max(dp[i-1][j], dp[i][j-1])），再判断是否为回文串
# 两个字母相同，dp[i][j] = dp[i-1][j-1] + 1; 不同：dp[i][j] = 0
#   dp[i][j]储存的就是最大公共子串的长度
class Solution3:
    # 有问题，覆盖不全
    def longestPalindrome(self, s):
        maxlen = 0
        maxend = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        sc = s[::-1]
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == sc[j]:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                # print(dp[i][j], 'dppppp')

                if dp[i][j] > maxlen:
                    prev = len(s) - j - 1       # 倒置前j指向的字符串首位的下标
                    if prev + dp[i][j] - 1 == i:  # 倒置前j指向的字符串尾部的下标：prev + dp[i][j] -1
                        maxlen = dp[i][j]
                        maxend = i

        maxsubstring = s[maxend - maxlen + 1:maxend + 1]

        return maxsubstring


class Solution4:            # 超时，增加分隔符后极大增加了数据量
    def longestPalindrome(self, st):
        if len(st) <= 1:
            return st

        s = '-'
        for element in st:
            s += element + '-'

        res = ''
        for i in range(1, len(s) - 1):
            length = min(len(s[:i]), len(s[i:-1]))
            # left = s[:i][:-length-1:-1]
            left = s[i - length:i][::-1]
            right = s[i + 1:i + length + 1]
            # print(i, '-->', length, left, '|', s[i], '|', right)
            for j in range(min(i, length), 0, -1):
                if left[:j + 1] == right[:j + 1]:
                    tmp = left[:j + 1][::-1] + s[i] + right[:j + 1]
                    # print('i=', i,'-->','j=',j, 'indice=',min(i, length))
                    res = tmp if len(tmp) > len(res) else res
        # print(res)
        # res = res1 if len(res1) >= len(res2) else res2
        return res.replace('-', '')


if __name__ == '__main__':
    # s = 'cabadiuidogiopp'
    s = 'abc435cba'
    s = 'abb'
    # s = "bbbaaaabbbdiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
    # s = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    output = Solution3().longestPalindrome(s)
    print(output)


# class Solution:
#     def longestPalindrome(self, s):
#         if len(s) == 1:
#             return s
#         if len(s) == 0:
#             return ''
#         if len(s) == 2 and s[0] == s[1]:
#             return s
#         if len(set(s)) == len(s):
#             return s[0]
#         res2 = ''
#         res1 = ''
#         for i in range(1, len(s)-1):
#             if s[i-1] == s[i] or s[i+1] == s[i]:
#                 res2 = s[i] * 2
#             length = min(len(s[:i]), len(s[i:-1]))
#             left = s[:i][:-length-1:-1]
#             right = s[i+1:i+length+1]
#             # print(i, '-->', length, left, '|', s[i], '|', right)
#             indice = min(i, length)
#             for j in range(indice):
#                 if left[:j+1] == right[:j+1]:
#                     # print('i=', i,'-->','j=',j, 'indice=',indice)
#                     tmp = s[i-(j+1):i+(j+1)+1]
#                     res1 = tmp if len(tmp) > len(res1) else res1
#         res = res1 if len(res1) >= len(res2) else res2
#         return res
