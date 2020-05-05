# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-26 23:02:06
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-14 19:48:08


"""无重复字符的最长子串"""


class Solution2:
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        start = 0
        strings_map = {}
        for cursor in range(len(s)):
            if s[cursor] in strings_map:
                # 更新start为map中重复字符的下一个字符的索引
                start = max(strings_map[s[cursor]] + 1, start)
            # 更新maxLength
            maxLength = max(cursor - start + 1, maxLength)
            # 更新cursor对应的字符最新map映射
            strings_map[s[cursor]] = cursor
        return maxLength

class Solution1:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        maxLength = 0
        start = 0
        for i in range(length):
            window = s[start:i + 1]
            maxLength = max(len(window), maxLength)
            if i + 1 != length:
                for indice, element in enumerate(window):
                    if element == s[i + 1]:
                        start = (i + 1) - len(window) + indice + 1
                        break
            else:
                break
        return maxLength


class Solution3:        # "abcfabcebb"
    def lengthOfLongestSubstring(self, s):
        res = 0
        start = 0
        st = {}
        for i in range(len(s)):
            if s[i] in st:
                start = max(start, st[s[i]] + 1)
            res = max(res, i - start + 1)
            st[s[i]] = i
            print(start, i, res, '   |', s[i], '-->', st[s[i]], st)
        return res


# class Solution1:
#     def lengthOfLongestSubstring(self, s):
#         length = len(s)
#         maxLength = 0
#         start = 0                                   # 初始为0，遇重复字符后更新为重复字符在滑窗中的位置对应的索引
#         cursor_window = 0                           # 滑窗中重复字符相对于整个字符串的索引位置指针
#         length_cur_window = 0                       # 滑窗长度记录指针
#         cursor_map = {}                             # window中的字符与索引映射
#         longestStr = ''                             # 定义存储最长字符串的变量
#         for i in range(length):
#             # print('i:', i)
#             # print('start:', start)
#             window = s[start:i+1]                               # 当前滑窗切片
#             longestStr = window if len(window) > len(longestStr) else longestStr
#             length_cur_window = len(window)
#             # print('substring:', window)
#             maxLength = max(length_cur_window, maxLength)       # 滑窗长度

#             if i + 1 != length:                     # 判断是否索引超限(i为最后一个字符索引时，i+1超限)
#                 if s[i+1] not in window:
#                     # 如果滑窗尾部字符的下一个字符不在滑窗中，则继续循环
#                     continue
#                 else:
#                     # 否则，更新重复字符在滑窗中的索引位置，并将该索引+1作为下一个滑窗的start
#                     # print('From index={},substring repeated! length={}'.format(i+1, maxLength))
#                     # window中循环确认重复字符所在位置
#                     for indice, element in enumerate(window):
#                         if element == s[i+1]:
#                             cursor_window = (i + 1) - length_cur_window + indice
#                             break
#                     # 更新滑窗start为重复字符在window中的绝对索引，cursor+1
#                     start = cursor_window + 1
#                     # print('start updated:', start)
#             else:
#                 break
#         print("Longest substring length without repeating is ", maxLength, '-->', longestStr)
#         return maxLength


if __name__ == '__main__':
    # s = "pwwsdkuiosew"
    s = 'dvdfabmnqweczxyaiuop'
    # s = "abcfabcebb"
    output = Solution2().lengthOfLongestSubstring(s)
    print(output)
