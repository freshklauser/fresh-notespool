# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-11 09:19:31
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-11 09:40:05

'''{description}
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，
编写一个函数判定它们是否只需要一次(或者零次)编辑。
示例 1:
    输入:
    first = "pale"
    second = "ple"
    输出: True
'''


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) > len(second):
            first, second = second, first

        nf = len(first)
        ns = len(second)

        if ns - nf > 1:
            return False

        if first == second:
            return True

        for i in range(nf):
            if first[i] != second[i]:
                if ns == nf:
                    return first[i + 1:] == second[i + 1:]
                else:
                    return first[i:] == second[i + 1:]

        return nf + 1 == ns


if __name__ == '__main__':
    s = "dab"
    t = "acb"
    res = Solution().oneEditAway(s, t)
    print(res)
