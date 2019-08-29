# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-07-26 16:12:26
# @Last Modified by:   klaus
# @Last Modified time: 2019-07-27 14:17:44

from socket import *

# 1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
sendAddr = ("192.168.1.103", 8080)

# 3. 从键盘获取数据
sendData = input('请输入要发送的数据')

# 4. 发送数据到指定的电脑上
unpSocket.sendto(sendData, sendAddr)

# 5. 关闭套接字
udpSocket.close()