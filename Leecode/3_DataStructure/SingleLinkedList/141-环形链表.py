# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-01 23:25:24
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 00:48:45

'''环形链表
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which
represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
'''


class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def hasCycle(self, head) -> bool:
        if not head:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
