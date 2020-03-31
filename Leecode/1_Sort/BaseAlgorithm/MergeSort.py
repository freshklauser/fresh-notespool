# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-04 17:30:43
# @Last Modified by:   klaus
# @Last Modified time: 2020-03-31 09:59:16

'''
归并排序：
将列表分割成小单位长度的子列表，
然后将两个有序子列表表合并成一个有序表。归并排序算法依赖于归并操作。

性质：
1、时间复杂度：O(nlogn)  *****
2、空间复杂度：O(n)
3、稳定排序
4、非原地排序
'''

# from heapq import merge

' 递归方式 --> 归并排序 '


class Solution:
    ''' 递归方式 '''

    def MergeSort(self, arr):
        if len(arr) < 2:
            return arr
        # 使用二分法将数列分两个,递归分割
        mid = len(arr) // 2
        left_arr = self.MergeSort(arr[:mid])
        right_arr = self.MergeSort(arr[mid:])
        # # 或者调用 heapq.merge方法直接合并排序
        # res = list(merge(left_arr, right_arr))
        # return res
        # 调用 自定义的合并排序运算
        return self.Merge(left_arr, right_arr)

    def Merge(self, left_arr, right_arr):
        ''' 合并算法
        借助辅助列表res，依次比较两个数组中的第一个元素，每次pop最小的首个元素添加到res中
        '''
        res = []
        while left_arr and right_arr:
            if left_arr[0] <= right_arr[0]:
                res.append(left_arr.pop(0))
            else:
                res.append(right_arr.pop(0))
        # 当至少一个为空之后，直接添加该列表中剩余的所有元素到res中
        res += left_arr or right_arr
        return res


' 非递归方式 --> 归并排序 '
class Solution2:
    '''
    将数组分为单个元素组成的len(arr)个subarr，对子数组两两归并排序，根据low和subarr的长度
    确定mid和high待合并的两个数组 [low:mid),[mid:high)
    '''
    def MergeSort(self, arr):
        sub_len = 1
        while sub_len < len(arr):                       # 只要subarr个数小于len(arr),继续分割
            # print("当前待合并的子数组长度： ", sub_len)
            # 第一轮sub_arr元素个数为1的两个数组排序后合并依次，第二轮sub_arr元素个数为2的两个数组排序后苯丙，以此类推
            low = 0
            while low < len(arr):                       # low向上更新后不能超过数组长度上限
                mid = low + sub_len                     # [low,mid)
                high = min(low + 2 * sub_len, len(arr))  # [mid, high)
                if mid < high:
                    # 对当前两个子数组[low,mid)与[mid,high)归并和排序，合并后的数组索引为[mid,high]
                    self.Merge(arr, low, mid, high)
                low = high  # # 更新 low ,即next 两个待归并数组   或者 low += 2 * i
            # 对当前sub_len长度的子数组进行归并与组内排序后，子数组长度*2, 继续下一轮合并
            sub_len *= 2
        return arr

    def Merge(self, arr, low, mid, high):
        """合并两个已排序好的列表，产生一个新的已排序好的列表"""
        left = arr[low:mid]
        right = arr[mid:high]
        res = []
        i = 0           # left的下标
        j = 0           # right的下标
        # 不使用pop方法，采用不断更新两个列表索引i，j的方法
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:] or right[j:]        # # 当一个为空后，将另一个的剩余元素直接添加到res中
        arr[low:high] = res                 # 替换arr[low:high]的数据为res对应的数据


if __name__ == '__main__':
    arr = [12, 433, 45, 2, 671, 4, 24, 67, 34, 10, 5]
    print(arr)
    res = Solution2().MergeSort(arr)
    print(res)
