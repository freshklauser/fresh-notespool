# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-03-23 09:07:18
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-28 11:01:15

'''{876-链表的中间节点}
思路：
    先遍历获得链表长度
    再遍历至middle处
'''


class ListNode:
    """docstring for ListNod   def __init__(self, arg):"""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNone(self, head):
        """ 常规思路：先遍历获取长度，再取middle """
        length = 0
        cursor = head
        while cursor:
            length += 1
            cursor = cursor.next
        mid = length // 2
        middle = head
        while mid:
            mid -= 1
            middle = middle.next
        return middle

    def middleNone_fast_slow_cursor(self, head):
        """ 快慢指针 """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
