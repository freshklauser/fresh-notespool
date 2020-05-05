# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-03 21:22:35
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-03 23:13:15


'''链表求和：两数相加 II
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
思路1：
    栈  分别入栈-->依次取出加法 留意进位 -->链表
思路2：
    短链表补齐零-->转数字-->加法-->转链表
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers_stack(self, l1, l2):
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1)
            l1 = l1.next
        # print([node.val for node in stack1])
        while l2:
            stack2.append(l2)
            l2 = l2.next

        # 依次出栈，相加，构造链表
        cursor = None
        flag = 0
        while stack1 or stack2 or flag:
            x = stack1.pop().val if stack1 else 0
            y = stack2.pop().val if stack2 else 0
            sum_val = x + y + flag
            flag = sum_val // 10

            node = ListNode(sum_val % 10)
            node.next = cursor
            cursor =node

        return cursor


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 or l2

        shorter = self.get_length(l1)
        longer = self.get_length(l2)
        if shorter >= longer:
            shorter, longer = longer, shorter
            l1, l2 = l2, l1
        diff = longer - shorter
        # 短链表头部补零节点
        l1 = self.add_zero_head(l1, diff)
        # 链表转换为数字
        num1 = self.list_to_int(l1)
        num2 = self.list_to_int(l2)
        # 相加后整型数字转回链表
        num = num1 + num2
        link = self.int_to_list(num)
        return link

    def add_zero_head(self, listnode, num_zero):
        cursor = listnode
        while num_zero:
            root = ListNode(0)
            root.next = cursor
            cursor = root
            num_zero -= 1
        return cursor

    def get_length(self, listnode):
        cursor = listnode
        length = 0
        while cursor:
            print('-->', cursor.val)
            cursor = cursor.next
            length += 1
        print('Length: ', length)
        return length

    def list_to_int(self, listnode):
        num = 0
        cursor = listnode
        while cursor:
            num = num * 10 + int(cursor.val)
            cursor = cursor.next
        # print('Number: ', num)
        return num

    def int_to_list(self, number):
        cursor = ListNode(None)
        while number:
            node_val = number % 10
            node = ListNode(node_val)
            node.next = cursor.next
            cursor.next = node
            number //= 10
        return cursor.next


if __name__ == '__main__':
    # r1 = ListNode(0)
    k1 = ListNode(2)
    k2 = ListNode(1)
    k3 = ListNode(5)
    k1.next = k2
    k2.next = k3

    l1 = ListNode(9)
    l2 = ListNode(1)
    l3 = ListNode(5)
    l4 = ListNode(4)
    l5 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    solution = Solution()
    res = solution.addTwoNumbers_stack(k1, l1)
    solution.get_length(res)

    # # solution.get_length(l1)
    # res = solution.addTwoNumbers(k1, l1)
    # solution.get_length(res)
    # num = solution.list_to_int(l1)
    # new = solution.int_to_list(num)
    # solution.get_length(new)
