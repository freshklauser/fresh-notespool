from threading import Thread
from socket import *
'''
window IP: 10.180.164.134
ubuntu IP: 10.180.164.149
'''
# 收数据 然后打印
def recData():
    recvInfo = udpSocket.recfrom(1024)
    print(">>{}:{}".format(recvInfo[1], recvInfo[0]))
    
# 检测键盘，发数据
def sendData():
    sendInfo = input("<<")
    udpSocket.sendto(sendInfo.encode('gb2312'), (XXIP, XXport))
    
udpSocket = None
destIp = ""
destPort = 0

def main():
    global udpSocket
    global destIp
    global destPort
    
    destIp = input('对方的IP:')
    destPort = int(input('对方的port:'))
    
    # 创建套接字
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind("", 4567)
    
    # 创建线程
    tr = Thread(target=recvData)
    ts = Thread(target=sendData)
    
    tr.start()
    ts.start()
    
    tr.join()
    ts.join()
    
if __name__ == '__main__':
    main()