# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-04 17:03:52
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-15 11:01:58

'''
冒泡排序
思路： 相邻元素比较，大的放后面，一轮比较下来，最大的就在最后
    1、把第一个元素与第二个元素比较，如果第一个比第二个大，则交换他们的位置。
    2、继续比较第二个与第三个元素，如果第二个比第三个大，则交换他们的位置….
    以此类推
    我们对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，
    这样一趟比较交换下来之后，排在最右的元素就会是最大的数。
    除去最右的元素，我们对剩余的元素做同样的工作，如此重复下去，直到排序完成。
性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序
'''


def BubbleSort(arr):
    if len(arr) < 2:
        return arr

    for i in range(len(arr)):
        swap_flag = False                   # 是否交换位置
        for j in range(len(arr) - i - 1):       # end：len(arr)-i-1，注意边界问题
            tmp = arr[j]
            if arr[j + 1] < arr[j]:           # 前值 > 后值，交换位置
                swap_flag = True            # True:交换了位置
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
        if not swap_flag:                   # 如果都没有交换过位置，直接退出for loop
            break
    return arr


if __name__ == '__main__':
    arr = [12, 433, 45, 2, 67, 4]
    res = BubbleSort(arr)
    print(res)
