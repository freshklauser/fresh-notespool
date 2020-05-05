# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-13 15:43:04
# @Last Modified by:   klaus
# @Last Modified time: 2020-03-13 15:46:27

'''{description}
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
示例:
    s = "3[a]2[bc]", 返回 "aaabcbc".
    s = "3[a2[c]]", 返回 "accaccacc".
    s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
思路：栈
    num存储数字，res存储字母
    [时:(num, res)入栈； ]时:(num, res)出栈-->注意出栈算法
'''


class Solution:
    def decodeString(self, s: str) -> str:
        num, res = 0, ""
        stack = []

        for element in s:
            if element == "[":
                stack.append((num, res))
                num, res = 0, ""
            elif element == "]":
                "todo: 出栈运算: res = top_element[1] + res * top_element[0]"
                top_element = stack.pop()
                res = top_element[1] + res * top_element[0]
            elif "0" <= element <= "9":
                num = num * 10 + int(element)       # 可以处理k为多位数的情况
            else:
                res += element
        return res


if __name__ == '__main__':
    s = "2[abc]3[cd]ef"
    res = Solution().decodeString(s)
    print(res)
