# -*- coding: utf-8 -*-
# @Author: F1684324
# @Date:   2019-06-06 16:12:44
# @Last Modified by:   sniky-lyu
# @Last Modified time: 2019-11-07 22:18:57

'''
[map(function, iterable1, iterable2)]
    map(function,iterable1,iterable2)，function中的参数值不一定是一个x，
    也可以是x和y，甚至多个；后面的iterable表示需要参与function运算中的参数值，
    有几个参数值就传入几个iterable

[filter(function, sequence)]
    filter函數，过滤掉序列中不符合函数条件的元素,function可以是匿名函数
    或者自定义函数，它会对后面的sequence序列的每个元素判定是否符合函数条件，
    返回TRUE或者FALSE，从而只留下TRUE的元素；sequence可以是数组、列表或者字符串等

[reduce(function, iterable)]
    from functools import reduce
    reduce函数对一个序列进行压缩运算，得到一个值，在functools中。function必须传
    入两个参数，iterable可以是列表或者元组
'''
import time

def dict_map(s):
    # 5-Excellent, 4-Good, 3-OK, 2-Bad, 1-Worse
    dictSeq = {'5': 'Excellent', '4': 'Good',
               '3': 'OK', '2': 'Bad', '1': 'Worse'}
    return dictSeq[s]


def dataReceiveErrorMap(s):
    # 5-Excellent, 4-Good, 3-OK, 2-Bad, 1-Worse
    if s not in (0,1,2):
        print("Error: there is no matching error code defined, please double check when receiving data.")
        s = 2
    s = s if isinstance(s, str) else str(s)
    dictSeq = {'0': {"code": "0904000", "message": "数据接收正常", "source": "192.168.1.18", "timestap": int(time.time() * 1000)},
               '1': {"code": "0904001", "message": "数据请求超时", "source": "192.168.1.18", "timestap": int(time.time() * 1000)},
               '2': {"code": "0904002", "message": "数据请求其他异常", "source": "192.168.1.18", "timestap": int(time.time() * 1000)}
               }
    return dictSeq[s]


if __name__ == '__main__':
    # out = list(map(dataReceiveErrorMap(1), 1))
    out = dataReceiveErrorMap(3)
    print(out)

    '''++++++++++++++ map() +++++++++++++ '''
    # out1 = list(map(dict_map, str(535124)))
    # # ['Excellent', 'OK', 'Excellent', 'Worse', 'Bad', 'Good']
    # print(out1)
    # x = [1, 2, 3, 4, 5]
    # y = [2, 3, 4, 5, 6]
    # out2 = list(map(lambda x, y: (x * y) + 2, x, y))
    # # [4, 8, 14, 22, 32]
    # print(out2)

    # '''++++++++++++++ filter() +++++++++++++ '''
    # import numpy as np
    # x = np.arange(1, 50, 2)
    # out3 = list(filter(lambda x: x % 3 == 0, x))
    # # [3, 9, 15, 21, 27, 33, 39, 45]
    # print(out3)

    # '''++++++++++++++ reduce() +++++++++++++ '''
    # from functools import reduce
    # x = [3, 5, 1, 2, 7]
    # # x = np.array([3, 5, 1, 2, 7])
    # out4 = reduce(lambda x, y: x * 10 + y, x)
    # # 35127
    # # 先计算头两个元素：f(2, 3)，结果为5；
    # # 再把结果和第3个元素计算：f(5, 4)，结果为9；
    # # 再把结果和第4个元素计算：f(9, 5)，结果为14；
    # # 再把结果和第5个元素计算：f(14, 6)，结果为20；
    # # 由于没有更多的元素了，计算结束，返回结果20
    # print(out4)
