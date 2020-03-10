# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-02-26 17:43:39
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 22:57:47

# Definition for singly-linked list.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        root = ListNode(0)               # 定义头结点
        cursor = root                   # 定义头结点指针(cursor:当前指针)
        flag = 0                        # 定义进位 0 or 1
        while l1 or l2:
            # 对位相加且判定是否进位
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sumVal = x + y + flag
            flag = sumVal // 10                # flag = 1 if s>=10 else 0

            sumNode = ListNode(sumVal % 10)    # 定义对位相加后的对应和节点，取余即为node.val

            cursor.next = sumNode       # 当前指针指针指向sumNode
            cursor = sumNode            # 移动当前指针至sumNode节点

            # 判断l1.和l2是否为None, 非None则赋值为下一个节点
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        # 循环结束后判断carry值，如果为1，则需要将当前指针指向ListNode(1)
        if flag == 1:
            cursor.next = ListNode(1)
            cursor = ListNode(1)

        return root.next


if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    another1 = ListNode(5)
    another2 = ListNode(6)
    another3 = ListNode(4)
    another1.next = another2
    another2.next = another3

    res = Solution().addTwoNumbers(node1, another1)
    output = []
    while res:
        output.append(res.val)
        res = res.next
    print(output)
