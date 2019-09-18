# -*- coding: utf-8 -*-
# @Author: F1684324
# @Date:   2019-09-18 10:02:53
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-09-18 11:01:17
# ------------------------------------------------------------------------------
# Description: example of bfs algrithm
# bfs: 优先检查一度朋友关系，一度朋友关系检查结束之后才会去检查二度朋友关系
#      如果找到一个则直接返回值
# ------------------------------------------------------------------------------


from collections import deque    # 线性表的模块


# 首先定义一个创建图的类，使用邻接矩阵
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.order = []  # visited order
        self.neighbor = {}

    def add_node(self, node):
        key, val = node
        if not isinstance(val, list):
            print('节点输入时应该为一个线性表')    # 避免不正确的输入
        self.neighbor[key] = val

    # 宽度优先算法的实现
    def BFS(self, root):
        # 首先判断根节点是否为空节点
        if root is not None:
            search_queue = deque()
            search_queue.append(root)
            visited = []
        else:
            print('root is None')
            return -1

        while search_queue:
            person = search_queue.popleft()
            print('person: ', person)
            self.order.append(person)
            # if self.is_N(person):
            #     print('search sucess.')
            #     return 1

            if (person not in visited) and (person in self.neighbor.keys()):
                search_queue += self.neighbor[person]   # 将节点的value都加入到search_queue中
                print(search_queue)
                visited.append(person)                  # visited存储的只有node的key

    # 深度优先算法的实现
    def DFS(self, root):
        # 首先判断根节点是否为空节点
        if root is not None:
            search_queue = deque()
            search_queue.append(root)
            visited = []
        else:
            print('root is None')
            return -1

        while search_queue:
            person = search_queue.popleft()
            self.order.append(person)

            if (person not in visited) and (person in self.neighbor.keys()):
                tmp = self.neighbor[person]
                tmp.reverse()

                for index in tmp:
                    search_queue.appendleft(index)

                visited.append(person)

    def clear(self):
        self.order = []

    def node_print(self):
        for index in self.order:
            print(index, end=' ')

    def is_N(self, element):
        return element == 'N'


if __name__ == '__main__':
    # 创建一个二叉树图
    g = Graph()
    g.add_node(('A', ['B', 'H']))
    g.add_node(('B', ['D', 'G']))
    g.add_node(('H', ['F']))
    g.add_node(('G', ['M', 'N']))
    g.add_node(('N', ['X', 'Y']))
    print(g.neighbor)
    # {'A': ['B', 'C'], 'B': ['D', 'G'], 'C': ['F'], 'G': ['M', 'N'], 'N': ['X', 'Y']}

    # 进行宽度优先搜索
    g.BFS('A')
    print('bfs:')
    g.node_print()
    g.clear()

    # # 进行深度优先搜索
    # print('\n\ndfs:')
    # g.DFS('A')
    # g.node_print()
    # print()
