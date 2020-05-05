# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-02 16:07:20
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 18:03:27

'''复制带随机指针的链表 Copy List with Random Pointer
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
Example 1:
    Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
思路： 遍历获得新旧节点交替的链表，拆链获得deepcopy的链表副本
'''


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList_recursive(self, head: 'Node') -> 'Node':
        '''递归方法 -- 链表深拷贝
        Arguments:
            head: 'Node' {[type]} -- [description]
        '''
        if head == None:
            return None

        if head in self.visited:
            return self.visited[head]

        node = Node(head.val, None, None)
        self.visited[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

    def copyRandomList(self, head):
        '''深拷贝， 新旧节点交替，完善random指针引用, 拆链
        A.random=B, 则A'.random=B'
        Arguments:
            head {[type]} -- [description]
        '''
        if not head:
            return None

        # Step-1: 遍历链表，获得新旧交替连接的新链表
        cursor = head
        while cursor:
            # 1. 复制节点，并重新引用链接
            link = Node(cursor.val, None, None)
            link.next = cursor.next
            cursor.next = link
            # 3. 移动cursor指针到步骤1中保存的节点
            cursor = link.next

        # Step-2: 遍历Step-1创建的新旧交替链表，完善复制节点的random指针引用
        cursor = head
        while cursor:
            # A.random=B, 则A'.random=B' （其中B'=A.random.next）
            cursor.next.random = cursor.random.next if cursor.random else None
            # 移动指针：跳过副本节点，只遍历原有链表的节点
            cursor = cursor.next.next

        # Step-3: 拆链表，获得原始链表和副本结点构成的新链表
        old_cursor = head
        new_cursor = head.next
        root = head.next
        while old_cursor:
            # 更改 原始链表 和 副本链表 的指针 （新链表时构建的链表的尾节点，需要判断None）
            old_cursor.next = old_cursor.next.next
            new_cursor.next = new_cursor.next.next if new_cursor.next else None
            # 移动指针：移动新旧指针cursor至对应链表的下一个结点 (右移)
            old_cursor = old_cursor.next
            new_cursor = new_cursor.next

        return root


def view(listnode):
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
    r1 = Node(0)
    k1_node1 = Node(21)
    k1_node2 = Node(13)
    k1_node3 = Node(55)
    r1.next = k1_node1
    k1_node1.next = k1_node2
    k1_node2.next = k1_node3
    k1 = r1.next
    res = Solution().copyRandomList(k1)
    view(res)
    # k1_node4 = Node(111)
    # k1_node3.next = k1_node4
    # view(k1)
    # view(res)
