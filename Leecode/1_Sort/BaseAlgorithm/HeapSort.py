# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2020-03-31 10:38:38
# @Last Modified by:   KlausLyu
# @Last Modified time: 2020-03-31 13:51:19

'''{堆排序}
堆排序是一个效率要高得多的选择排序，首先把整个数组变成一个最大堆，然后每次从堆顶取出最大的元素，
这样依次取出的最大元素就形成了一个排序的数组。堆排序的核心分成两个部分:
    第一个是新建一个堆，
    第二个是弹出堆顶元素后重建堆。
新建堆不需要额外的空间，而是使用原来的数组，一个数组在另一个维度上可以当作一个完全二叉树（除了最后一层之外
其他的每一层都被完全填充，并且所有的节点都向左对齐）.
    对于下标为i的元素，他的子节点是2*i+1和2*i+2（前提是没有超出边界）。
    在新建堆的时候从左向右开始遍历，当遍历到一个元素的时候，重新排列从这个元素节点到根节点的所有元素，
保证满足最大堆的要求（父节点比子节点要大）。遍历完整个数组的时候，这个最大堆就完成了。
在弹出根节点之后（把根节点的元素和树的最底层最右侧的元素互换），堆被破坏，需要重建。
从根节点开始和两个子节点比较，如果父节点比最大的子节点小，那么就互换父节点和最大的子节点，
然后把互换后在子节点位置的父节点当作新的父节点，和它的子节点比较，如此往复直到最后一层，这样最大堆就重建完毕了。
'''

class HeapSort(object):
    def __init__(self,array):
        self.array = array
        self.heapSize = len(array)

    def max_heapify(self,heap,heapSize,root):
        left = 2 * root + 1
        right = left + 1
        lager = root
        if left < heapSize and heap[left] > heap[lager]:
            lager = left
        if right < heapSize and heap[right] > heap[lager]:
            lager = right
        if root != lager:
            heap[lager],heap[root] = heap[root],heap[lager]
            self.max_heapify(heap,heapSize,lager)

    def build_max_heap(self):
        for i in range(self.heapSize//2,-1,-1):
            self.max_heapify(self.array,self.heapSize,i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heapSize-1,-1,-1):
            self.array[i],self.array[0] = self.array[0],self.array[i]
            self.max_heapify(self.array,i,0)
        return self.array

if __name__ == '__main__':
    array = [2,5,3,89,65,4,23,6,21,12]
    res = HeapSort(array).heap_sort()
    print(res)
