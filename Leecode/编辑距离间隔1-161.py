# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-10 20:40:46
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-10 21:01:25


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # 巧妙： 确保s是短字符串
        if len(s) > len(t):
            s, t = t, s

        ns, nt = len(s), len(t)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if nt == ns:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        # 如果for loop中转移至相等，则只需要判断nt是否比ns大1即可，是则True,否则false(包含了s==t的情况)
        return ns + 1 == nt


class Solution1:
    '''
    笨方法：枚举可能的情况
    '''

    def isOneEditDistance(self, s: str, t: str) -> bool:

        shorter = s if len(s) <= len(t) else t
        longer = t if len(s) <= len(t) else s

        if shorter == longer:
            return False

        m = len(shorter)
        n = len(longer)

        if n - m > 1:
            return False

        k = 0
        if m == n and m != 0:
            while True:
                if shorter[k] != longer[k] and shorter[k +
                                                       1:] == longer[k + 1:]:
                    return True
                elif shorter[k] != longer[k] and shorter[k + 1:] != longer[k + 1:]:
                    return False
                else:
                    k += 1
                    if k == m:
                        return False
        if m == n and m == 0:
            return False

        i = 0
        if n - m == 1 and m != 0:
            while True:
                if shorter[i] != longer[i] and shorter[i:] == longer[i + 1:]:
                    return True
                elif shorter[i] != longer[i] and shorter[i:] != longer[i + 1:]:
                    return False
                else:
                    i += 1
                    if i == m:
                        return True
        if n - m == 1 and m == 0:
            return True


if __name__ == '__main__':
    s = "dab"
    t = "acb"
    res = Solution().isOneEditDistance(s, t)
    res1 = Solution1().isOneEditDistance(s, t)
    print(res)
