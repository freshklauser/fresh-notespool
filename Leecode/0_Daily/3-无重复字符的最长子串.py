# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-02 11:38:56
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 16:03:05


"""[无重复字符的最长子串]
Given a string, find the length of the longest substring without repeating characters.

Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

思路：
    hash表 + 双指针，每一次遍历时存储 item 对应的索引到 hash表中
    当item在hash表中出现过时，更新 start为 max(index_in_hash + 1, start)
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        maxlength = 0
        start = 0
        items = dict()
        for i, item in enumerate(s):
            if item in items.keys():
                start = max(items[item] + 1, start)

            maxlength = max(maxlength, i - start + 1)
            items[item] = i
        return maxlength


if __name__ == '__main__':
    s = "abcabcbe"
    # s = 'pwwkew'
    res = Solution().lengthOfLongestSubstring(s)
    print(res)
