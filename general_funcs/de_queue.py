# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:34:19 2019
@author: Klaus
------------------------------------------------------------
Note the front(list_index=-1) and back(list_index=0) of a queue 
"""
class Queue:
    def __init__(self):
        self.__queue=[]
        self.__size=0     
    def __str__(self):
        return ''.join([str(i) for i in self.__queue])
    def size(self):
        return self.__size
    def is_empty(self):
        return self.__size<=0
    def enqueue(self,data):
        self.__queue.append(data)
        self.__size += 1
    def dequeue(self):
        if self.is_empty():
            return -1
        else:
            self.__size -= 1
            return self.__queue.pop(0)

class Dequeue:
    def __init__(self):
        self.__queue=[]
        self.__size=0
    def __str__(self):
        return ''.join([str(i) for i in self.__queue])
    def is_empty(self):
        return self.__size==0
    def size(self):
        return self.__size
    def insert_front(self, data):
        self.__queue.append(data)
        self.__size += 1
    def insert_back(self, data):
        self.__queue.insert(0, data)
    def delete_front(self):
        if self.is_empty():
            return -1
        self.__size -= 1
        return self.__queue.pop()
    def delete_back(self):
        if self.is_empty():
            return -1
        self.__size -= 1
        return self.__queue.pop(0)
        
    
