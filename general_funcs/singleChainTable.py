# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:31:22 2019

@author: klaus
"""

class Node():
    '''Definition for singly-linked list.'''
    __slots__ = ['_item','_next']               # Limit the argument of class
    def __init__(self, item):
        self._item = item
        self._next = None                       # The cursor points to None defaultly.
    def getItem(self):
        return self._item
    def getNext(self):
        return self._next
    def setItem(self,newitem):
        self._item = newitem
    def setNext(self, newnext):
        self._next = newnext
        
class SingleChainTable():
    def __init__(self):
        '''Initialize the chaintable to empty'''
        self._head = None                       # _head is a Node(including 2 args and 4 funcs)
        self._size = 0
    def isEmpty(self):
        '''Check if the single chaintable is empty'''
        return self._head == None
    def size(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    def traveser(self):
        current = self._head
        while current != None:                  # Traverser all the element
            print(current.getItem())
            current = current.getNext()
    def add(self, item):
        '''Add element in the head of chaintable'''
        temp = Node(item)                       # Refer to class 'Node'
        temp.setNext(self._head)
        self._head = temp
    def append(self, item):
        '''Add element in the tail of chaintable'''
        temp = Node(item)
        if self.isEmpty():
            self._head = temp                   # Add as the first element if it's empty
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()     # Traverse the chaintable
            current.setNext(temp)
    def search(self, item):
        '''check if item is in chainitem'''
        current = self._head
        founditem = False
        while current != None and not founditem:
            if current.getItem() == item:
                founditem = True
            else:
                current = current.getNext()    # Traverse the chaintable
        return founditem
    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getItem() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            print('{} is not in the chaintable!'.format(item))
            raise ValueError
    def remove(self, item):
        current = self._head
        previous = None
        while current != None:
            if current.getItem() == item:
                if not previous:
                    # if current is the node to remove, repalce current node with nex node
                    self._head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                break
            else:
                previous = current
                current = current.getNext()       
    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos >self.size():
            self.append(item)
        else:
            temp = Node(item)
            count = 1
            previous = None
            current = self._head
            while count < pos:
                count += 1
                previous = current
                current = current.getNext()
            previous.setNext(temp)
            temp.setNext(current)
            
if __name__ == '__main__':
    a = SingleChainTable()
    for i in range(1,10):
        a.append(2**i)
    print(a.size())
    print('-------------------------')
    a.traveser()
    print('-------------------------')
    print(a.search(8))
    print(a.index(2))         # index:1  (header's index=0)
    print('-------------------------')
    a.remove(4)
    a.traveser()
    a.insert(4,9999)
    a.traveser()
    