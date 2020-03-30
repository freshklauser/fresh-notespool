# -*- coding: utf-8 -*-
# @Author: sniky-lyu
# @Date:   2020-03-13 20:12:53
# @Last Modified by:   Administrator
# @Last Modified time: 2020-03-29 13:56:28

''' 需要用 while True: try...except:break '''


'''
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了
N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，
不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。
请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。

Input Param
n               输入随机数的个数
inputArray      n个随机整数组成的数组
Return Value
OutputArray    输出处理后的随机整数


注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。

样例输入解释：
样例有两组测试
第一组是3个数字，分别是：2，2，1。
第二组是11个数字，分别是：10，20，40，32，67，40，20，89，300，400，15。

输入描述:
输入多行，先输入随机整数的个数，再输入相应个数的整数

输出描述:
返回多行，处理后的结果

'''

# while True:
#     try:
#         total = int(input())
#         res = set()
#         for i in range(total):
#             res.add(int(input()))
#         for ele in sorted(res):
#             print(ele)
#     except Exception:
#         break


def main(s):
    n = len(s)
    res = ""
    for i in range(n):
        # A --> Z
        if s[i].isupper():
            if s[i] == "Z":
                res += "a"
            else:
                res += chr(ord(s[i]) + 1).lower()
        elif s[i].islower():
            if s[i] == "z":
                res += "A"
            else:
                res += chr(ord(s[i]) + 1).upper()
        elif "0" <= s[i] <= "9":
            res += str((int(s[i]) + 1) % 10)
        # break
    return s


print("10".isdigit())
print("a".isupper())
print("a".islower())
s2 = "TJm5Jpgv9"
s2.replace
# res1 = main(s1)
res2 = main(s2)
# while True:
#     try:
#         s1= input()
#         # res1 = main(s1)
#         res2 = main(s2)
#         # print(res1)
#         # print(res2)
#     except:
#         break
