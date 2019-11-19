# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-19 14:00:18
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-19 14:08:35

import time
import threading

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
threads.append(thread1)
thread2 = myThread(2, "Thread-2", 2)
threads.append(thread2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
    # 开始线程：Thread-1
    # 开始线程：Thread-2
    # Thread-1: Tue Nov 19 14:01:57 2019
    # Thread-1: Tue Nov 19 14:01:58 2019
    # Thread-2: Tue Nov 19 14:01:58 2019
    # Thread-1: Tue Nov 19 14:01:59 2019
    # Thread-2: Tue Nov 19 14:02:00 2019
    # Thread-1: Tue Nov 19 14:02:00 2019
    # Thread-1: Tue Nov 19 14:02:01 2019
    # 退出线程：Thread-1
    # Thread-2: Tue Nov 19 14:02:02 2019
    # Thread-2: Tue Nov 19 14:02:04 2019
    # Thread-2: Tue Nov 19 14:02:06 2019
    # 退出线程：Thread-2
    # 退出主线程


# 开启新线程
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
    # 开始线程：Thread-1
    # Thread-1: Tue Nov 19 14:00:59 2019
    # Thread-1: Tue Nov 19 14:01:00 2019
    # Thread-1: Tue Nov 19 14:01:01 2019
    # Thread-1: Tue Nov 19 14:01:02 2019
    # Thread-1: Tue Nov 19 14:01:03 2019
    # 退出线程：Thread-1
    # 开始线程：Thread-2
    # Thread-2: Tue Nov 19 14:01:05 2019
    # Thread-2: Tue Nov 19 14:01:07 2019
    # Thread-2: Tue Nov 19 14:01:09 2019
    # Thread-2: Tue Nov 19 14:01:11 2019
    # Thread-2: Tue Nov 19 14:01:13 2019
    # 退出线程：Thread-2
    # 退出主线程

print ("退出主线程")