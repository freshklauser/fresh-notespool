# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-07-26 14:36:06
# @Last Modified by:   klaus
# @Last Modified time: 2019-07-26 14:46:31

import socket

'''tcp socket(tcp通信的套接字)'''
s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s_tcp)
# <socket.socket fd=536, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

'''udp socket（udp通信的套接字）'''
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(s_udp)
# <socket.socket fd=540, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0>
