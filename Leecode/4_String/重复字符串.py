# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2020-04-05 21:31:02
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2020-04-05 22:49:57


"""重复字符最长串
题目：
    给定一串字符，里面有些字符有连续出现的特点，请寻找这些连续出现字符中最长的串，
    如果最长的串有多个，请输出字符ASCII码最小的那一串。
    例如：输入aaabbbbbcccccccczzzzzzzz，输出cccccccc。
思路：
    1) 反向遍历长度(len - len(set(arr)) + 1)
        2) 遍历set(arr)
            如果：当set(arr)遍历完一遍之后出现 arr 能被 element*cur_len 分割开(splited_length > 1),
                说明该重复串为最长的重复串
                (1) 如果set(arr)中不止一个同样长度的最长重复串，则取ascii码小的串
                (2) dicts[lenght] = cur_element
                (3) 将 flag 置为 True
        判断flag， False则继续下一轮for循环
                   True则跳出外层循环
    返回值=v*k
"""


def maxRepeatStr(arr):
    if not arr:
        return arr

    # 去重后的每个元素的重复字符串可能的最大长度
    len_up_border = len(arr) - len(set(arr)) + 1
    # 缓存遍历，最大长度和当前元素（分别初始化为1和最大ASCII码对应的字符）
    max_len = 1
    cur_element = chr(127)
    # res[max_len] = min_ascii_element_with_max_length
    res = {}
    # 长度反向遍历的跳出标识
    flag = False

    for i in range(len_up_border, 0, -1):
        for s in set(arr):
            spt = s * i
            # 以 spt 分割原始字符串作为判断依据:如果spt在arr中存在，则分割后长度>1; 若不存在，分割后长度=1
            splited = arr.split(spt)
            if len(splited) > 1:
                # print('i-->', i, 's-->', s, 'splited-->', splited)
                max_len = max(max_len, i)
                cur_element = min(cur_element, s)
                res[i] = cur_element
                flag = True
        if flag:
            break
    output = [v * k for k, v in res.items()]
    return output[0]


if __name__ == '__main__':
    # arr = 'aaabbbbbcccccccczzzzzzzz'
    # arr = 'sssssssssssssssssssssssssssssssdikllislppppppposadyppppppppppppsdfffffffffffffn..........lsdf'
    arr = 'aaaaaaaaaaaaaasdffdiiiiiiiiiiiiii--------------558/**'
    # print('--->', arr.split('aaaaaaaaaaaaaa'), len(arr.split('aaaaaaaaaaaaaa')))
    res = maxRepeatStr(arr)
    print(res, ord(res[0]))
    # print(len(res))
    # print(len('aaaaaaaaaaaaaa'))
