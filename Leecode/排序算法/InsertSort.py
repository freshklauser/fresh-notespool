# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-04 15:58:25
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-15 11:02:15

'''
性质：1、时间复杂度：O(n2)  2、空间复杂度：O(1)  3、稳定排序  4、原地排序
思路：
    1、从数组第2个元素开始抽取元素。
    2、把它与左边第一个元素（从后往前）比较，如果左边第一个元素比它大，则继续与左边第二个元素（从后往前）比较下去，
      直到遇到不比它大的元素，然后插到这个元素的右边。
    3、继续选取第3，4，….n个元素,重复步骤 2 ，选择适当的位置插入。
'''


def InsertSort(arr):
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        inserted = arr[i]                       # 待插入元素
        cursor = i - 1                          # 前向遍历的指针初始索引
        while cursor + 1:                       # cursor+1，确保index=0的元素可以被比较到
            if arr[cursor] > inserted:
                arr[cursor + 1] = arr[cursor]     # 大，则元素后裔一位
                cursor -= 1                     # 同时，指针前移一位
            else:
                break                           # 小，则推出while, 插入元素到 cursor+1 索引处即可
        arr[cursor + 1] = inserted

    return arr


if __name__ == '__main__':
    arr = [12, 433, 45, 2, 67, 4]
    res = InsertSort(arr)
    print(res)
