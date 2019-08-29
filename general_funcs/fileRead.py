# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:26:38 2018

@author: Administrator
"""

# -*- coding:utf-8 -*-
text_file = r"test.txt"
# open()
f = open(text_file, "rb")
# 以文件起始位置作为相对位置，偏移8个字节长度
f.seek(8, 0)
# 输出当前指针偏移量
pos = f.tell()
print(pos)          # 8
# 读取8个字节长度的文本，范围为[8,16）
text_to_number = f.read(8)
print(text_to_number)       # b'BBBBBBBB'
# 输出当前指针偏移量，可以观测到read()也会造成文件指针偏移
pos = f.tell()          # 16
print(pos)
# 只有在“二进制”模式下操作文件时才能定位到其他位置，否则只能以文件起始位置作为定位
# 二进制模式下，以当前位置为原点，偏移9个字节长度
f.seek(9, 1)
# 读取100个字节长度的文本，范围为[24,124）
text_to_all = f.read(100)
print(text_to_all)      # b'DDDDDDDEEE'
pos = f.tell()
print(pos)        #   35

f.close()