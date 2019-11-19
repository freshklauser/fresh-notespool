# -*- coding: utf-8 -*-
# @Author: KlausLyu
# @Date:   2019-11-19 14:27:25
# @Last Modified by:   KlausLyu
# @Last Modified time: 2019-11-19 15:53:11

import threading
import time

def run():
    print(threading.current_thread().getName(), "开始工作")
    time.sleep(0.5)       # 子线程停 x s
    print("子线程 {} 工作完毕".format(threading.current_thread().getName()))

thread_list = []

for i in range(3):
    t = threading.Thread(target=run,)
    thread_list.append(t)
    t.setDaemon(True)   # 把子线程设置为守护线程，必须在start()之前设置

for t in thread_list:
    t.start()

cnt = 0
try:
    while any([t.isAlive() for t in thread_list]) == True:
        # 只要thread_list中有一个线程在运行，则继续运行子线程；反之(即子线程均不在运行) 继续主线程至结束
        # 即：确保子线程程序执行完 (最后只有一个alive的线程：主线程)
        # 如果 any --> all,则只要有一个线程不是 alive状态就直接跳出子线程继续运行主线程，主线程结束则所有子线程也结束(包含未运行完的子线程)
        cnt += 1
    print(cnt)
    print("主线程结束了！")
    print(threading.active_count())  # 输出活跃的线程数
    # active_count:
    # The list includes daemonic threads, dummy thread objects created by
    # current_thread(), and the main thread. It excludes terminated threads and
    # threads that have not yet been started.
except KeyboardInterrupt:
    print('stopped by keyboard')



# # time.sleep(1)     # 主线程在程序啟動停1秒


# t.start()
# t.join()      同一個for循環裡
    # Thread-1 开始工作
    # 子线程工作完毕
    # Thread-2 开始工作
    # 子线程工作完毕
    # Thread-3 开始工作
    # 子线程工作完毕
    # 主线程结束了！
    # 1



# for i in range(3):
#     t = threading.Thread(target=run,)
#     thread_list.append(t)
#     # t.setDaemon(True)   # 把子线程设置为守护线程，必须在start()之前设置
#     t.start()
# for t in thread_list:
#     t.join()
    # Thread-1 开始工作
    # Thread-2 开始工作
    # Thread-3 开始工作
    # 子线程工作完毕
    # 子线程工作完毕
    # 子线程工作完毕
    # 主线程结束了！
    # 1


