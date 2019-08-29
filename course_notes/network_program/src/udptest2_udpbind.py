# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-07-27 14:20:03
# @Last Modified by:   klaus
# @Last Modified time: 2019-07-27 15:46:09

from socket import *

# 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

# 接收时绑定本地相关信息，若不绑定，则系统会随机分配
bindArr = ("", 6666)    # "" 表示本机的任何一个ip
udpSocket.bind(bindArr)

# 等待接受对方发送的数据
'''本机使用recvfrom之前需要绑定本机的接受IP和port,否则会系统随机分配端口，
   导致发送端指定的接收端口如6666与本机接收端的动态端口不一致'''
recvData = udpSocket.recvfrom(1024)     # 本次接受最大字节数为1024
content, destInfo = recvData
# 接收到传输的数据后打印出来
print(recvData)
# 中文需要解码，通常选 utf-8解码，不行的话换成 gb2312解码
print(("内容: {}; 地址: {}").format(content.decode("utf-8"), destInfo))
# print(("内容: {}; 地址: {}").format(content.decode("gb2312"), destInfo))

# 关闭socket
udpSocket.close()