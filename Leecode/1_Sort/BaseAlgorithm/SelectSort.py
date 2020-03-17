# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-03-04 15:36:41
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 16:34:41

'''
选择排序：
    1、时间复杂度：O(n^2)
    2、空间复杂度：O(1)
    3、非稳定排序
    4、原地排序

思路：
    （1）找到数组中最小的那个元素，
    （2）将它和数组的第一个元素交换位置(如果第一个元素就是最小元素那么它就和自己交换)
    （3）在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。
     如此往复，直到将整个数组排序。这种方法我们称之为选择排序。
前面排过序的成为有序区，后面没排的是无序区
'''

def SelectSort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        # 嵌套循环：遍历一遍找到最小元素的索引
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                # 更新最小值下标
                min_index = j

        # 交换arr[i] 与 arr[min_index]的位置 python交换位置的简单写法
        arr[min_index], arr[i] = arr[i], arr[min_index]
        # tmp = arr[min_index]
        # arr[min_index] = arr[i]
        # arr[i] = tmp

    return arr


if __name__ == '__main__':
    arr = [12,433,45,2,67,4]
    res = SelectSort(arr)
    print(res)
