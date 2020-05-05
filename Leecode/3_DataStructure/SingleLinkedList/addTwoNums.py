# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-26 17:43:39
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-12 17:10:23

# Definition for singly-linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    ''' 结果保存在新的链表sumNode中 '''

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化一个头结点，将头结点赋予指针cursor
        head = ListNode(0)
        cursor = head

        carry = 0                       # 保存进位 0 or 1
        while l1 or l2:
            x = l1.val if l1 else 0     # l1为空则x=0, 不为空则x=l1.val
            y = l2.val if l2 else 0
            sumval = x + y + carry
            # 进位
            carry = sumval // 10
            # 指针节点指向sumval的Node
            cursor.next = ListNode(sumval % 10)
            # 将指针移动到sumNode节点, 此时sumNode节点==cursor.next
            cursor = cursor.next

            # 移动l1和l2两个节点，下一轮while继续相加
            # 不为空则更新到下一个节点，为空(若当前l1为空则不存在l1.next)则继续while
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # 判断最后一次while之后的进位，为1则将当前指针指向ListNode(1)
        if carry == 1:
            cursor.next = ListNode(1)
        return head.next


if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(9)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    another1 = ListNode(5)
    another2 = ListNode(6)
    another3 = ListNode(8)
    another1.next = another2
    another2.next = another3

    res = Solution().addTwoNumbers(node1, another1)
    output = []
    while res:
        output.append(res.val)
        res = res.next
    print(output)
