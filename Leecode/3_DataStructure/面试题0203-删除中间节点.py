# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-02 00:47:05
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 00:47:41

'''删除中间节点
实现一种算法，删除单向链表中间的某个节点（除了第一个和最后一个节点，不一定是中间节点），假定你只能访问该节点。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
