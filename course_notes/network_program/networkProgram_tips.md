[TOC]

# 一、基础

## 1. 端口

端口是用来区分进程的，标记唯一进程的方式。（同一台电脑上进程号是`PID`）

端口通过端口号来标记，只有整数，范围 `[0, 65535]`

在同一个OS中，端口不允许相同，如果某个端口已经被使用，那么在这个进程释放这个端口之前，其他进程不能使用这个端口。原因：端口用来区分一个进程，如果相同，那么久不能把数据发送给正确的进程。

- 知名端口（well known ports）

  范围：`[0, 1023]`

  ```
  80端口：分配给HTTP服务
  21端口：分配给FTP服务
  ```

- 动态端口

  范围：`[1024, 65535]`

查看端口：`netstat -an `

## 2. IP地址

`IP`地址在逻辑上标记唯一一台电脑。 包括 网络地址和主机地址。

- 主机号最后不能使用 0 和 255
  - 255： 广播地址，如192.168.119.255
  - 0： 网路号，如 192.168.119.0

> <font color=mediumpurple>`2**10: k; 2**20: M； 2**30：G；  2**32: 4G`</font>
>
> `IPV4: 4个字节IP地址，如下图右，功32个Byte`
>
> `IPV6: 16进制表示`

<div align=center><img src=".\img\tcpip协议簇.png" width="48%"/>&nbsp<img src=".\img\IP地址分类.png" width="50%"/></div>

<div align=center><img src=".\img\网络通信.png" width="80%"/></div>

- A类IP地址

  组成部分：1字节的网络地址和3字节主机地址

  范围：`1.0.0.1 --- 126.255.255.254`

- B类IP地址

  组成部分：2字节的网络地址和2字节主机地址

  范围：`128.1.0.1 ---191.255.255.254`

- C类IP地址

  `范围： 192.0.1.1 --- 223.255.255.254`

  `组成部分： 3字节的网络地址 + 1字节的主机地址。网络地址的最高位必须是 110`

- D类IP地址 -- 用于多点广播

  第一个字节以`1110`开始，是一个专门保留的地址，视频会议就是用的多播

- 私有IP

  用于局域网使用，不在公网中使用

  `10.0.0.0  --- 10.255.255.255`

  `172.16.0.0 --- 172.31.255.255`

  `192.168.0.0 --- 192.168.255.255`

- 回路测试IP

  `127.0.0.1 --- 127.255.255.255`

  如 `127.0.0.1`可以代表本机IP地址，用`http://127.0.0.1`就可以测试本机中配置的`web`服务器

## 3. Socket

多个电脑之间的进程通信。

通讯需要确定好 IP、端口和通信协议。`udp和tcp都是全双工，能收能发`

### 1. socket属性和方法

`socket.socket([family[, type[, proto]]]) -> socket object`

> `Family: 通信协议的协议族，可以选择 AF_INET（用于Internet进程间通信）或者AF_UNIX（用于同一台机器进程间通信），实际工作中常用 AF_INET`
>
> `Type: 套接字类型，可以使 SOCK_STREAM（流式套接字，主要用于 TCP协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）`

> `family 指定应用程序使用的通信协议的协议族，对于TCP/IP协议族，该参数为AF_INET`
>
> > `socket.AF_UNIX: 只能够用于单一的Unix系统进程间通信`
> >
> > `socket.AF_INET: 服务器之间网络通信`
> >
> > `socket.AF_INET6: IPv6`

- 创建一个 `tcp socket`（`tcp 套接字`）

  特点：<font color=tomato>`tcp`通信慢，但是稳定，不太可能丢失数据</font>

  ```
  import socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  ```

- 创建一个 `udp socket` ( `udp`套接字 )

  特点：<font color=tomato>`udp`通信快，但是不稳定，容易丢失数据</font>

  ```
  s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  ```

`socket 方法 ：`[<font color=mediumpurple>`Refer links here`</font>](https://blog.csdn.net/zzyandzzzy/article/details/72236388)

> `s.bind(address):将套接字绑定到地址, 在AF_INET下,以元组（host_ip,port）的形式表示地址. 本机ip可以用 "" 表示`
>
> `s.close(): 关闭套接字`
>
> - `udp`方法
>
> <font color=tomato>`s.sendto(string[,flag],address):` </font>`发送UDP数据。将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数.`
>
> <font color=tomato>`s.recvfrom(bufsize[.flag]):`</font> `接受UDP套接字的数据。返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址(IP, port)。`
>
> - `tcp`方法
>
> `---`

### 2. 本机发送数据  `udpsocket.sendto`

- 实例1（**本机`windows`** 向 虚拟机`ubuntu` **发送**数据）：

1. 通信主体

   - 发送方：**`windows`**系统 ，`ipAddr:` <font color=tomato>`192.168.1.71`</font>,  端口(动态，随意设置)：<font color=tomato>`1234`</font>
   - 接收方：`ubuntu`虚拟机(网络：<font color=mediumpurple>桥接模式</font>), `ipAddr:`<font color=tomato>`192.168.1.57`</font>, 端口：<font color=tomato>`8080`</font>

   注意：在开始通信之前，需要确认发送方和接收方的`IP`能`ping`通

   ​	`windows:` `ping 192.168.1.57`

   ​	`ubuntu :` `ping 192.168.1.71`

2. 发送方程序（`py`文件 or 网络测试助手`A`）

   `py文件发送：` (结果如下图)

```
# 发送一般不需要绑定udp信息
from socket import *
udpSocket = socket(AF_INET, SOCK_DGRAM)
sendData = b"Today is Saturday!"   # 字节类型传输
receiverIpAddr = "192.168.1.57"	   # 接收方IP地址（此处为虚拟机ubuntu系统的IP地址）
receiverPort = 8080				  # 接收方端口地址（此处为虚拟机ubuntu系统网络测试助手的port）
# .sendto方法，以UDP协议发送sendData至receiverIpAddr的receiverPort对应的程序
udpSocket.sendto(sendData, (receiverIpAddr, receiverPort))
```

<div align=center><img src='.\img\udptest1_sendtoubuntu.png' width='55%'></div>	

​	`windows网络测试助手A(左图)` 发送至 `ubuntu网络助手B(右图)`，如下图

<div align=center><img src='.\img\sendA_windows.png' width='50%'>&nbsp<img src='.\img\receive_ubuntu.png' width='48.5%'></div>	

​	注意：同一程序多次发送给同一个`IP`和`port`时，发送方每次的`port`不一定相同，会随机分配动态端口，如下图红框所示：(该情况 未进行 `udp绑定信息`，因此每次发送分配的 `port` 时是动态端口) --- 下文会探讨

<div align=center><img src='.\img\动态port.png' width='48%'></div>	

- 实例2（**本机`windows`** 向 虚拟机`ubuntu` **发送**数据）--（给飞秋发送信息）

1. 飞秋发送信息基本格式： 

   `版本号：包编号:发送者姓名：发送者机器名：命令字：发送信息内容`  （其中前面的可以仿照下例随便写，命令字必须为 `32`）

   `1:1238605487:klaus:whoever_pc:32:Nice day!`

2. 飞秋个人信息事先查看联系人 `IP`和`端口`（飞秋系统设置中有默认端口：2425）

<div align=center><img src='.\img\feiq1.png' width='48%'>&nbsp<img src='.\img\feiq2.png' width='48.5%'></div>	

### 3. 本机接收数据 ` udpsocket.recvfrom`

- 实例 ： `udp`绑定信息接收

  - 接收方（本机）：**`windows`**系统 ，`ipAddr:` <font color=tomato>`192.168.1.71`</font>,  端口(代码中绑定)：<font color=tomato>`6666`</font>
  - 发送方：`ubuntu`虚拟机(网络：<font color=mediumpurple>桥接模式</font>), `ipAddr:`<font color=tomato>`192.168.1.57`</font>, 端口(动态，随意设置)：<font color=tomato>`8080`</font>

  数据流向： 虚拟机`ubuntu`系统网络测试助手 向 `windows`系统`python`程序发送数据并代码`print`

  1） `windows`系统中`python`程序代码 （运行后 等待发送方发送数据，接收到后`print`）

  ```
  from socket import *
  udpSocket = socket(AF_INET, SOCK_DGRAM)
  
  # 接收方绑定本地相关信息，若不绑定，则系统会随机分配
  bindArr = ("", 6666)    # "" 表示本机的任何一个ip
  udpSocket.bind(bindArr)
  
  # 等待接受对方发送的数据
  '''本机使用recvfrom之前需要绑定本机的接受IP和port,否则会系统随机分配端口，
     导致发送端指定的接收端口如6666与本机接收端的动态端口不一致'''
  recvData = udpSocket.recvfrom(1024)     # 本次接受最大字节数为1024
  
  # 接收到传输的数据后打印出来
  print(recvData)
  # 若含有中文需要解码，通常选 utf-8解码，不行的话换成 gb2312解码 （针对中文网站）
  print(("内容: {}; 地址: {}").format(content.decode("utf-8"), destInfo))
  # print(("内容: {}; 地址: {}").format(content.decode("gb2312"), destInfo))
  # 关闭socket
  udpSocket.close()
  ```

  2) `ubuntu`系统网络测试助手输入 接收方的`IP`和绑定的`port`，输入`data`并发送

  <div align=center><img src='.\img\udpbind.png' width='65%'></div>	

  3)  `windows`系统中`python`程序代码接收到数据后，`print`数据如下

  ```
  (b'networkprogramming\xe7\xbd\x91\xe7\xbb\x9c\xe7\xbc\x96\xe7\xa8\x8b', ('192.168.1.57', 8080))
  内容: networkprogramming网络编程; 地址: ('192.168.1.57', 8080)
  [Finished in 2.7s]
  ```

  接收到的数据元组包含两部分：<font color=tomato>数据正文内容</font> 和 <font color=tomato>发送方`IP`和`port`</font>

### 4. echo服务器 （回显服务器）

echo服务器，描述起来很简单，服务端收到什么，就给客户端发送什么。



### 5. 进程和线程

- 进程是操作系统资源分配的基本单位，而线程是任务调度和执行的基本单位
- 没有线程的进程可以看做是单线程的，如果一个进程内有多个线程，则执行过程不是一条线的，而是多条线（线程）共同完成的；线程是进程的一部分，所以线程也被称为轻权进程或者轻量级进程。

### 6. tftp过程分析

1. 怎么发送？怎么接受？

   `tftp协议`

2. d

   所有网络中传输的数据都必须以 大端  格式传输