# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-30 19:35:04
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-30 21:38:34

'''[约瑟夫环问题]
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，
因此最后剩下的数字是3。

示例 1：
    输入: n = 5, m = 3
    输出: 3
思路：
    list删除 取余 （这里不采用约瑟夫环的数学方法）
'''


class Solution:
    def lastRemaining(self, n, m):
        lst = list(range(n))
        index = 0
        while len(lst) > 1:
            index = (index + m - 1) % len(lst)
            lst.pop(index)
        return lst[0]


if __name__ == '__main__':
    n, m = 9, 5
    res = Solution().lastRemaining(n, m)
    print(res)
