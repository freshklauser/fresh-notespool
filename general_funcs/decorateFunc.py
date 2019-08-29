# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-08-19 10:35:50
# @Last Modified by:   klaus
# @Last Modified time: 2019-08-19 10:35:55


def timmer(func):
    # 定义装饰器，监控运行时间
    def wrapper(*arg, **kwargs):
        start_time = time.perf_counter()
        res = func(*arg, **kwargs)
        stop_time = time.perf_counter()
        print(">>>>>> Func %s, run time: %s <<<<<<" %
              (func.__name__, stop_time - start_time))
        return res
    return wrapper
