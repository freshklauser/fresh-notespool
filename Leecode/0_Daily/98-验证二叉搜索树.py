# -*- coding: utf-8 -*-
# @Author   : Administrator
# @DateTime : 2020/5/5 10:55
# @FileName : 98-验证二叉搜索树.py
# @SoftWare : PyCharm

"""验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
    输入:
        2
       / \
      1   3
    输出: true
思路：
    (1) 递归
    (2) DFS
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode):

        def bst(root, low=float('-inf'), high=float('inf')):
            if not root:
                return False
            print(low, 'low')
            print(high, 'high')
            cur = root.val
            if cur < low or cur > high:
                return False

            if not bst(root.left, low, cur):
                return False
            if not bst(root.right, cur, high):
                return False

            return True

        return  bst(root)


if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(1)
    node2 = TreeNode(7)
    node3 = TreeNode(3)
    node4 = TreeNode(8)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4

    res = Solution().isValidBST(root)
    print(res)
