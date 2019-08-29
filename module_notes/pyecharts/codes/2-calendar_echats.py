# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-06-19 16:42:00
# @Last Modified by:   klaus
# @Last Modified time: 2019-06-22 11:20:08


# 示例画出来的图显示不完整，不知道怎么解决；
# 是否可以x轴为星期，y轴为月份？？

import datetime
import numpy as np
import random
from pyecharts.charts import Calendar
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType
'''
print(np.random.randint(20, 100, 1))        # [55]
print(random.randint(20, 100))              # 40
'''

def calendar_example():
    begin = datetime.date(2018, 1, 1)
    end = datetime.date(2019, 1, 1)
    # data = [visualmap_opts
    #     [str(begin + datetime.timedelta(days=i)), random.randint(100, 2500)]
    #     for i in range((end - begin).days)
    # ]
    data = []
    for i in range((end - begin).days):
        temp = [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
        data.append(temp)
    # print(data)

    calend = (
        # 设置图的宽高和背景色
        Calendar(init_opts=opts.InitOpts(width='1300px', height='300px', bg_color='#7FFFAA', theme=ThemeType.CHALK))
        .add(series_name='', yaxis_data=data, calendar_opts=opts.CalendarOpts(range_='2018'))     # range_决定了时间尺度
        # .add(series_name='', yaxis_data=data, calendar_opts=opts.CalendarOpts(range_=['2018-1', '2018-7']))     # range_决定了时间尺度
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Calendar-2018年微信步数'),
            visualmap_opts=opts.VisualMapOpts(
                max_=25000,
                min_=100,
                range_size=[10,20],         # 不知道干嘛的
                orient='horizontal',
                is_calculable=True,
                is_piecewise=True,     # 颜色条是否分成pieces:True:pices, False:一根长条
                pos_top='230px',
                pos_left='100px',
                # pos_right='100px',
                # out_of_range=[0,50,100],   # 不知道干嘛的
                ),
            )
        )
    return calend

if __name__ == '__main__':
    calendar = calendar_example()
    calendar.render('calendar_echats.html')
    make_snapshot(snapshot, calendar.render('calendar_echats.html'), 'calendar_echats.png')
