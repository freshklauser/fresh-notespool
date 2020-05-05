# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-12 16:32:28
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-12 16:34:37

"""{description}
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
注意：
    num1 和num2 的长度都小于 5100.
    num1 和num2 都只包含数字 0-9.
    num1 和num2 都不包含任何前导零。
    你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
思路：
    ascii码转int后计算，减去基准"0"的ascii码
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        base = ord("0")
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        carry = 0                   # 进位 0 or 1
        while i >= 0 or j >= 0:     # 有一个遍历完就跳出
            n1 = num1[i] if i >= 0 else "0"
            n2 = num2[j] if j >= 0 else "0"
            nplus = ord(n1) - base + ord(n2) - base + carry
            carry = nplus // 10
            cur_n = nplus % 10
            res = chr(cur_n + base) + res   # res位置不能放在前面
            i -= 1
            j -= 1
        res = "1" + res if carry == 1 else res
        return res


if __name__ == '__main__':
    num1 = "99"
    num2 = "103"
    res = Solution().addStrings(num1, num2)
    print(res, num1, type(res))
