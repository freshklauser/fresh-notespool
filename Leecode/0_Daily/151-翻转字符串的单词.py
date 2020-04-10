# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-04-10 14:25:30
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-04-10 16:18:30

'''{151. 翻转字符串里的单词}
给定一个字符串，逐个翻转字符串中的每个单词。
示例 1：
    输入: "the sky is blue"
    输出: "blue is sky the"
思路：（最方便是直接字符串的api如reverseWords_1）
    双指针
'''

class Solution:
    def reverseWords(self, s):
        s = s.strip()
        res = ''
        if len(s) <= 1:
            return s
        i, j = len(s) - 1, len(s)
        while i > 0:
            if s[i] == ' ':
                res += s[i + 1:j] + ' '     # 第一个空格时，res += xxxx; 同时 j更新
                while s[i] == ' ':          # 判断s[i]是否还有空，从当前s[i]开始
                    i -= 1
                j = i + 1                   # s[i] 不为空后，更新j为当前单词的后一个位置
            i -= 1                          # 更新i
        res += s[:j]                        # 添加最后一个单词 s[:j]，此时 i=-1
        return res



    def reverseWords_1(self, s):
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    s = "  a good   example "
    res = Solution().reverseWords(s)
    print(res)
