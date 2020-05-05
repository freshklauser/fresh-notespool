# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-12 15:20:30
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-12 15:40:41

'''{description}
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
    左括号必须用相同类型的右括号闭合。
    左括号必须以正确的顺序闭合。
思路：
栈
'''
class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0: return False

        stack = []
        maps = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char not in maps.keys():
                stack.append(char)          # "("   "["   "{" 存入栈中
            else:
                top_stack = stack.pop() if stack else 0
                if maps[char] != top_stack:
                    return False
        return not stack


class Solution1:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

if __name__ == '__main__':
    s = "([)]"
    res = Solution().isValid(s)
    print(res)
