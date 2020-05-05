# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-05-02 18:40:13
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-05-02 21:16:45

'''链表求和 Sum Lists LCCI
    Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.
Tips:
    while l1 or l2 --> 知道加完l1和l2的所有值，最后判断flag确定是否添加ListNode(1)的尾结点
    不要用while l1 and l2 再针对剩下的l1或l2进位判断，比较繁琐，可能一直进位，代码与while主题右重复
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 or l2

        flag = 0
        node = ListNode(0)
        cursor = node
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_val = x + y + flag
            flag = sum_val // 10

            cursor.next = ListNode(sum_val % 10)
            cursor = cursor.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if flag == 1:
            cursor.next = ListNode(1)

        return node.next


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

    res = Solution().addTwoNumbers_2(node1, another1)
    # res = Solution().addTwoNumbers(node1, another1)
    output = []
    while res:
        output.append(res.val)
        res = res.next
    print(output)
