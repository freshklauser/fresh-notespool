# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-19 13:55:57
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-28 11:01:27

'''{409-最长回文串 与5-回文子串题目有区别}
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
注意:
    假设字符串的长度不会超过 1010。
示例 1:
    输入:
    "abccccdd"
    输出:
    7
解释:
    我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
思路：
   回文串特性：1个字符长度为奇数，其他均为偶数即可
   最长回文串 = 所有期数-1+所有偶数
'''

from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return n
        # hash统计单词出现次数
        hash_s = Counter(s)
        # print(hash_s)
        sum_even = 0
        sum_odd = 0
        flag = False
        for k, v in hash_s.items():
            if v % 2 == 0:
                sum_even += v
            else:
                flag = True
                sum_odd += v - 1
        if flag:
            res = sum_even + sum_odd + 1
        else:
            res = sum_even
        return res


if __name__ == '__main__':
    # s = "abccccdd"
    s = "bb"
    # s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    res = Solution().longestPalindrome(s)
    print(res)
