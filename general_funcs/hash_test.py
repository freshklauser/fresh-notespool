# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:44:59 2018

@author: Administrator
"""

'''
HASH算法（对某段信息打指纹，能够压缩信息,hash算法是不可逆的）
M ----> N  （M >> N）即压缩映射 N为固定长度
'''

import hashlib

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HASH文件
chunkSize = 4096                    # 每次读取文件的字节数
def hashFile(fileName):
    '''
    对文件做hashs
    '''
    h = hashlib.sha256()
    # 操作文件：按固定字节长度读
    with open(fileName, 'rb') as f:           # rb: 作为二进制文件读取
        while True:
            chunk = f.read(chunkSize)
            if not chunk:               # 当读文件到结尾处是，跳出循环
                break
            h.update(chunk)
    return h.hexdigest()            # 得到文件最终的hash值     



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HASH字符串
def hashStr(strInfo):
    h = hashlib.sha256()
    h.update(('hello world').encode('utf-8'))   
    # update方法要求对输入的字符串进行编码encode
    return h.hexdigest()            # 返回对应字符串最终的hash值


if __name__ == '__main__':
    print(hashStr('it\'s sunday today!'))
    print(hashStr('hello world!'))
    print(hashFile('regex.txt'))
    



