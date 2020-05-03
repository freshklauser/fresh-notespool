# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-05-02 23:06:39
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 23:10:13


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def partition(self, head, x):
        '''头插法
        所有小于x的结点都插入到头部
        '''
        if not (head and head.next):
            return head
        prev = head
        cursor = head.next
        while cursor:
            if cursor.data >= x:
                prev = cursor
                cursor = cursor.next
            else:
                prev.next = cursor.next
                cursor.next = head
                head = cursor
                cursor = prev.next
        return head


def view(listnode, node_type=Node):
    ''' 查看列表中的所有元素 '''
    if not isinstance(listnode, node_type):
        raise AttributeError("Node type of input is expected")
    link_str = ''
    while listnode is not None:
        if listnode.next is not None:
            link_str += str(listnode.data) + '-->'
        else:
            link_str += str(listnode.data)
        listnode = listnode.next
    print('The Linklist is: {}'.format(link_str))


if __name__ == '__main__':
    r1 = Node(None)
    k1_node1 = Node(121)
    k1_node2 = Node(13)
    k1_node3 = Node(55)
    k1_node4 = Node(513)
    k1_node5 = Node(12)
    r1.next = k1_node1
    k1_node1.next = k1_node2
    k1_node2.next = k1_node3
    k1_node3.next = k1_node4
    k1_node4.next = k1_node5
    k1 = r1.next
    view(k1)
    res = Solution().partition(k1, 40)
    view(res)