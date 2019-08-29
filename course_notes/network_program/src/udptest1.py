# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-07-27 11:43:16
# @Last Modified by:   klaus
# @Last Modified time: 2019-07-27 15:39:43

from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

# 绑定udp信息 -- 一般都是接收方的ip和port需要绑定
udpSocket.bind(("", 7789))

sendData = "Today is Saturday星期六!"        # 需要encode字节类型传输
# sendData1 = b"Tomorrow is Sunday!"        # 字节类型传输

receiverIpAddr = "192.168.1.57"
receiverPort = 8080

udpSocket.sendto(sendData.encode('utf-8'), (receiverIpAddr, receiverPort))
# udpSocket.sendto(sendData1, (receiverIpAddr, receiverPort))

# 接受信息
# recvData = udpSocket.recvfrom(1024)
# print(recvData)