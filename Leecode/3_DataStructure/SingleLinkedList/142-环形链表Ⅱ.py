# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-01 23:25:24
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 00:50:14


'''环形链表Ⅱ -- 环的入口位置
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents
the position (0-indexed) in the linked list where tail connects to. If pos is -1,
then there is no cycle in the linked list.
Note: Do not modify the linked list.
'''


class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        '''hash表, visited辅助空间'''
        if not head:
            return None
        visted = set()
        node = head
        while node.next:
            if node in visted:
                return node
            else:
                visted.add(node)
                node = node.next
        return None

    def detectCycle_twiceMeet(self, head):
        if not head:
            return None
        fast = slow = head

        while True:
            if not (fast.next and fast.next.next):
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                # 第一次相遇的节点
                break
        # 第一次相遇后fast从头开始移动，第二次相遇的点几位环的入口
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
