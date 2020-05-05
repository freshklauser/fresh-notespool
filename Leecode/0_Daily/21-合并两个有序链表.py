# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-05-01 15:33:37
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-01 23:24:20


class ListNode(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        self.new_head = ListNode(None)
        cursor = self.new_head
        while l1 and l2:
            if l1.data <= l2.data:
                cursor.next = l1
                l1 = l1.next
            else:
                cursor.next = l2
                l2 = l2.next
            # 移动指针cursor
            cursor = cursor.next
        # 其中一个为空后，将cursor直接指向剩余链表
        cursor.next = l1 or l2
        return self.new_head.next


def view_linkedlist(listnode):
    ''' 查看列表中的所有元素 '''
    if not isinstance(listnode, ListNode):
        raise AttributeError("ListNode type of input is expected")
    link_str = ''
    while listnode is not None:
        if listnode.next is not None:
            link_str += str(listnode.data) + '-->'
        else:
            link_str += str(listnode.data)
        listnode = listnode.next
    print('The Linklist is: {}'.format(link_str))


if __name__ == '__main__':
    root1 = ListNode(None)
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(3)
    l1_node3 = ListNode(5)

    root2 = ListNode(None)
    l2_node1 = ListNode(1)
    l2_node2 = ListNode(2)
    l2_node3 = ListNode(6)

    root1.next = l1_node1
    l1_node1.next = l1_node2
    l1_node2.next = l1_node3

    root2.next = l2_node1
    l2_node1.next = l2_node2
    l2_node2.next = l2_node3

    l1 = root1.next
    l2 = root2.next
    # print(l1.val, l2.next.val)

    res = Solution().mergeTwoLists(l1, l2)
    view_linkedlist(res)
    # print(type(res))
