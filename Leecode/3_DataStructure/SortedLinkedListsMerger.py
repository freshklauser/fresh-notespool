# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2020-04-13 14:09:02
# @Last Modified by:   win
# @Last Modified time: 2020-04-13 17:03:47

'''{合并K个有序链表}
Example:
Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
Output: 1->1->2->3->4->4->5->6
'''


class ListNode(object):
    """docstring for ListNode"""
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, linkedlists):
        pass

    def mergeTwoLists(self, list1, list2):
        '''两个有序链表合并
        Arguments:
            list1 {sorted linkedlist} -- [description]
            list2 {[sorted linkedlist]} -- [description]

        Returns:
            [merged sorted linkedlist] -- [description]
        '''
        head = cursor = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                pass

        return head.next

