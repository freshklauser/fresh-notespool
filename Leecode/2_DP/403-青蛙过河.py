# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-11 12:34:00
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 14:42:38

"""{description}
题目
一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。
青蛙可以跳上石头，但是不可以跳入水中。
给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 
开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。
如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 
另请注意，青蛙只能向前方（终点的方向）跳跃。
请注意：
    石子的数量 ≥ 2 且 < 1100；
    每一个石子的位置序号都是一个非负整数，且其 < 231；
    第一个石子的位置永远是0。
示例 1:
[0,1,3,5,6,8,12,17]
总共有8个石子。
第一个石子处于序号为0的单元格的位置, 第二个石子处于序号为1的单元格的位置,
第三个石子在序号为3的单元格的位置， 以此定义整个数组...最后一个石子处于序号为17的单元格的位置。
返回 true。即青蛙可以成功过河，按照如下方案跳跃：
跳1个单位到第2块石子, 然后跳2个单位到第3块石子, 接着
跳2个单位到第4块石子, 然后跳3个单位到第6块石子,
跳4个单位到第7块石子, 最后，跳5个单位到第8个石子（即最后一块石子）。

思路：dp
    dp_dict:跳到第i块石头的距离集合
"""


class Solution:
    def canCross(self, stones):
        if not stones:
            return False

        dp_dict = {}
        for i in stones:
            dp_dict[i] = set()                      # value保存跳到i石头的距离集合

        dp_dict[stones[0]].add(0)

        for STONE in stones:                        # 遍历stone
            for k in dp_dict[STONE]:                # 遍历stone对应的可到达距离
                for distance in [k - 1, k, k + 1]:  # 到达下一个stone的距离
                    if distance > 0 and STONE + distance in dp_dict.keys():
                        dp_dict[STONE + distance].add(distance)
        return dp_dict[stones[-1]] != set()


if __name__ == '__main__':
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    # stones = [0, 1, 2, 3, 4, 8, 9, 11]
    res = Solution().canCross(stones)
    print(res)

    from collections import defaultdict
    dp = defaultdict(list)
    for stone in stones:
        dp[stone]
