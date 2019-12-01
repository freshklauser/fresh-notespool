# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-11-19 13:34:59
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-19 13:59:43

import threading
import time
from time import ctime,sleep

def music(act):
    for i in range(2):
        print ("I was listening to %s. %s" %(act,ctime()))
        sleep(1)


def move(act):
    for i in range(2):
        print ("I was at the %s! %s" %(act,ctime()))
        sleep(5)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


class myThread (threading.Thread):
    '''从 threading.Thread 继承创建一个新的子类
    '''
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)


if __name__ == '__main__':
    music(u'爱情买卖')
    move(u'阿凡达')

    print ("all over %s" %ctime())
