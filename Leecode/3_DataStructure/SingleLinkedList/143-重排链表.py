# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-02 00:58:30
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 11:35:29

'''重排链表(间隔重排)
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.
Example 1:
    Given 1->2->3->4, reorder it to 1->4->2->3.

思路:
    Step-1: 找中心节点, 获取左右链表
    Step-2: 翻转右链表
    Step-3: 间隔合并 -- 注意合并的先后逻辑
'''


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        left, right, middle = self.get_middle(head)
        right = self.reverse(right)
        res = self.merge_interval(left, right)
        return res

    # Step-1: 找中心节点, 获取左右链表
    def get_middle(self, list_node):
        fast, slow = list_node, list_node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # midlle node
        middle_node = slow
        # 右链表
        right = slow.next
        # 左链表(裁剪过右链表内容的)
        slow.next = None
        left = list_node
        return left, right, middle_node

    # Step-2: 翻转右链表
    def reverse(self, list_node):
        pre_node = None
        cursor = list_node
        while cursor:
            tmp = cursor.next
            cursor.next = pre_node
            pre_node = cursor
            cursor = tmp
        return pre_node

    # Step-3: 间隔合并
    def merge_interval(self, left, right):
        head = Node(None)
        head.next = left
        while left and right:
            link = right
            right = right.next

            link.next = left.next
            left.next = link
            left = link.next
        return head.next

    def view(self, listnode):
        ''' 查看列表中的所有元素 '''
        if not isinstance(listnode, Node):
            raise AttributeError("Node type of input is expected")
        link_str = ''
        while listnode is not None:
            if listnode.next is not None:
                link_str += str(listnode.val) + '-->'
            else:
                link_str += str(listnode.val)
            listnode = listnode.next
        print('The Linklist is: {}'.format(link_str))


if __name__ == '__main__':
    r1 = Node(None)
    k1_node1 = Node(21)
    k1_node2 = Node(13)
    k1_node3 = Node(55)
    k1_node4 = Node(14)
    k1_node5 = Node(52)
    r1.next = k1_node1
    k1_node1.next = k1_node2
    k1_node2.next = k1_node3
    k1_node3.next = k1_node4
    k1_node4.next = k1_node5

    k1 = r1.next
    res = Solution().reorderList(k1)
    Solution().view(res)
    # print('``````````````````')
    # left, right, middle_node = Solution().get_middle(k1)
    # Solution().view(left)
    # Solution().view(right)
    # # print(middle_node.val)

    # # rev = Solution().reverse(left)
    # # Solution().view(rev)

    # res = Solution().merge_interval(left, right)
    # Solution().view(res)
