# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-31 09:02:21
# @Last Modified by:   Administrator
# @Last Modified time: 2020-04-05 13:08:20

'''{纯排序算法题目}
重点掌握：归并排序 和 堆排序
'''


class Solution:
    def sortArray(self, nums):
        ''' 调用定义的排序算法 '''
        return self.MergeSort(nums)

    def MergeSort(self, nums):
        ''' 归并排序: 长度为sub_len的两两子数组依次排序合并，每一轮sub_len*2 '''
        sub_len = 1
        while sub_len < len(nums):
            low = 0
            'TODO: 子数组归并排序'
            while low < len(nums):
                mid = low + sub_len
                high = min(mid + sub_len, len(nums))
                if mid < high:
                    # print(sub_len, '---', low,mid,high, nums[low:mid], nums[mid:high])
                    self.Merge(nums, low, mid, high)
                    # print('--->', nums)
                low = high
            sub_len *= 2
        return nums

    def Merge(self, arr, low, mid, high):
        ''' 合并算法: 合并两个*有序列表*left和right，产生一个新的已排序好的列表merged '''
        left = arr[low:mid]
        right = arr[mid:high]
        merged = []
        i, j = 0, 0             # 对应left和right数组的下标
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # left或right剩下的元素直接添加到
        merged += left[i:] or right[j:]
        arr[low:high] = merged


if __name__ == '__main__':
    nums = [5, 1, 1, 2, 0, 6, 8, 100, 0]
    res = Solution().sortArray(nums)
    print(res)
