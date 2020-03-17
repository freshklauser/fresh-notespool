# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-05 16:13:13
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 16:53:24

' 快速排序 '
'''
快速排序是一种交换排序
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

对冒泡排序的有效改进。快速排序是一种不稳定的排序算法，即多个相同的值的相对位置也许会在算法结束时产生变动。
步骤：
    1）挑选基准值 base
    2）分割：所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面
    3）递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序
'''

def QuickSort(arr):
    if len(arr) < 2:
        return arr
    base = arr[0]
    left = [x for x in arr[1:] if x < base]
    right = [x for x in arr[1:] if x > base]
    res = QuickSort(left) + [base] + QuickSort(right)
    return res

if __name__ == '__main__':
    arr = [12,33,21,132,45,2,67,4]
    # left = [x for x in arr[1:] if x < arr[0]]
    # right = [x for x in arr[1:] if x > arr[0]]
    # subleft_right = [x for x in right if x < right[0]]
    # subright_right = [x for x in right if x > right[0]]
    # print(left, right, subleft_right, subright_right)
    res = QuickSort(arr)
    print(res)