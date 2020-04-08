# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-04-05 13:10:56
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-05 13:21:46

'''有效括号的嵌套深度 1111
给你一个「有效括号字符串」 seq，请你将其分成两个不相交的有效括号字符串，A 和 B，并使这两个字符串的深度最小。

    不相交：每个 seq[i] 只能分给 A 和 B 二者中的一个，不能既属于 A 也属于 B 。
    A 或 B 中的元素在原字符串中可以不连续。
    A.length + B.length = seq.length
    深度最小：max(depth(A), depth(B)) 的可能取值最小。

划分方案用一个长度为 seq.length 的答案数组 answer 表示，编码规则如下：

    answer[i] = 0，seq[i] 分给 A 。
    answer[i] = 1，seq[i] 分给 B 。

思路：
    要让A和B的最大深度最小，关键就是，AB的深度谁都别涨太快。
    涨深度的时候，谁比较浅，我就给谁涨。降的时候，谁比较深，我就给谁降
    “涨深度”就是'('，来一个左括号，那深度就涨一格，所以AB谁浅就给谁涨。深度一样的话呢，就随便给涨一个。
    涨完了得降，“降深度”就是右括号，右括号来了谁深先降谁。
'''


class Solution:
    def maxDepthAfterSplit(self, seq):
        res = []
        a = b = 0     # subSeq_A 和 subSeq_B 的初始深度设为0
        for i, s in enumerate(seq):
            if s == "(":
                if a <= b:
                    a += 1
                    res.append(0)
                else:
                    b += 1
                    res.append(1)
            elif s == ")":
                if a >= b:
                    a -= 1
                    res.append(0)
                else:
                    b -= 1
                    res.append(1)
        return res


if __name__ == '__main__':
    seq = "()((()(((((())))))))()"
    res = Solution().maxDepthAfterSplit(seq)
    print(res)
