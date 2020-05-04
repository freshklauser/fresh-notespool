# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/4 16:09
# @FileName : 45-跳跃游戏Ⅱ.py
# @SoftWare : PyCharm

""" 跳跃游戏Ⅱ
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
示例:
    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
思路：
    贪心算法 （青蛙一次跳1格是dp问题）
    遍历时更新能跳到的最大位置max_pos, 更新max_pos后
"""


class Solution:
    def jump(self, nums):
        boundary = 0
        max_pos = 0
        step = 0

        for i, value in enumerate(nums):
            if i == len(nums) - 1:
                return step
            # 更新索引i时能到达的最远距离
            max_pos = max(max_pos, i + value)
            if i == boundary:
                # 当i遍历到当前的边界时，更新边界为max_pos,同时step += 1
                boundary = max_pos
                step += 1
        return step

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4, 5]
    res = Solution().jump(nums)
    print(res)
