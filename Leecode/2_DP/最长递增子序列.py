# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 15:15:28
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-11 15:40:02

'''{description}
自己在笔记本上举一个例子一步一步算一下，找到合适的转换关系
'''


def longsetIncSubString(arr):
    if not arr:
        return 0

    # dp[i]: 以arr[i]结尾的最长上升子序列的长度
    # 单个字符，子序列长度为1, 全部初始化为1, 不是0
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):          # 确保j<i, arr[j]是在arr[i]前面的数
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j - 1] + 1)

    # 从dp中找出最大值
    max_len = max(dp)

    return max_len


if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    res = longsetIncSubString(arr)
    print(res)
