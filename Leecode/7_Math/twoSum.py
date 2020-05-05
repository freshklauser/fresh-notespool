# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-02-26 16:52:43
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-16 10:37:27


class Solution1:
    def twoSum(self, nums, target):
        for index_i, num_i in enumerate(nums):
            for index_j, num_j in enumerate(nums):
                if index_i != index_j and num_i + num_j == target:
                    output = [index_i, index_j]
                    return output


class Solution2:
    def twoSum(self, nums, target):
        dicts = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num not in dicts:
                dicts[num] = index
            else:
                return [dicts[another_num], index]
        return None


class Solution3:
    def twoSum(self, nums, target):
        """
        Arguments:
            nums {[type]} -- [description]
            target {[type]} -- [description]
        """
        # 根据num大小对索引排序
        sorted_id = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = len(nums) - 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        while sum_result != target:
            if sum_result > target:         # sum大，则减小大的值的索引
                tail -= 1
            elif sum_result < target:       # sum小，则增大小的值的索引
                head += 1
            sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
        return [sorted_id[head], sorted_id[tail]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    output = Solution2().twoSum(nums, target)
    print(output)

    # sorted_id = sorted(range(len(nums)), key=lambda x: nums[x])
    # print(sorted_id)
