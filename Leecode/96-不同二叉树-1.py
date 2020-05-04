# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-05 21:31:17
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-03-05 23:24:00

'''
题目：给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树
  1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
问题是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：
    G(n): 长度为n的序列的不同二叉搜索树个数。
    F(i, n): 以i为根的不同二叉搜索树个数(1≤i≤n)。
F(i,n)=G(i−1)⋅G(n−i)
G(n) = sum(F(i,n))  (1<=i<=n)
---> G(n) = sum(G(i−1)⋅G(n−i))   (1<=i<=n)
---> G(n) 的值依赖于 G(0)…G(n−1)
refer: https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode/
'''


class Solution:
    def numTrees(self, n):
        """
        Arguments:
            n {[int]} -- 序列的长度
        Returns:
            [int] -- [description]
        """
        # G(n): 长度为n的序列的不同二叉搜索树个数。
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]


if __name__ == '__main__':
    n = 4
    res = Solution().numTrees(n)
    print(res)
