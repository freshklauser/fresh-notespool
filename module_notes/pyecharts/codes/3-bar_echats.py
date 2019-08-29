# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-06-19 14:51:01
# @Last Modified by:   klaus
# @Last Modified time: 2019-06-22 08:38:10

'''
https://pyecharts.org/#/zh-cn/quickstart
 ['charts',
 'commons',
 'components',
 'datasets',
 'globals',
 'options',
 'render',
 'scaffold',
 'types']
'''
import datetime
import random
from pyecharts import charts
from pyecharts import options as opts   # options配置项
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot  # 使用 snapshot-selenium 渲染图片
# 需下载chromedriver.exe并拷贝至anaconda3根目录
from pyecharts.charts import Page
from pyecharts.globals import ThemeType
# 内置主题类型可查看 pyecharts.globals.ThemeType

'''
# 使用主题
print(dir(ThemeType))
# ['BUILTIN_THEMES', 'CHALK', 'DARK', 'ESSOS', 'INFOGRAPHIC', 'LIGHT', 'MACARONS',
# 'PURPLE_PASSION', 'ROMA', 'ROMANTIC', 'SHINE', 'VINTAGE', 'WALDEN', 'WESTEROS',
# 'WHITE', 'WONDERLAND'
# ------------------------------------------------------------------
'''
page = Page()           # 使用page则只需要最后page进行render即可

# 也可以采用如下的链式调用,  使用options配置项
xtick = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
ytickA = [5, 20, 36, 10, 75, 90]
ytickB = [15, 6, 45, 20, 35, 66]
# 在使用 Pandas&Numpy 时，请确保将数值类型转换为 python 原生的 int/float。
# 比如整数类型请确保为 int，而不是 numpy.int32
labelA = "商家A"
labelB = "商家B"
bar = (
    charts.Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK))  # 使用主题
    .add_xaxis(xtick)
    .add_yaxis(labelA, ytickA)
    .add_yaxis(labelB, ytickB)
    # 设置title
    .set_global_opts(title_opts={'text': '主标题', 'subtext': '副标题'})
)
# bar.render('bar_echats.html')           # 渲染网页
# 渲染图片： snapshot-selenium
# make_snapshot(snapshot, bar.render('bar_echats.html'), "bar_echarts.jpeg")
page.add(bar)

begin = datetime.date(2018, 1, 1)
end = datetime.date(2019, 1, 1)
data = []
for i in range((end - begin).days):
    temp = [str(begin + datetime.timedelta(days=i)),
            random.randint(1000, 25000)]
    data.append(temp)
calend = (
    charts.Calendar()
    # range_决定了时间尺度
    .add(series_name='', yaxis_data=data, calendar_opts=opts.CalendarOpts(range_='2018'))
    # .add(series_name='', yaxis_data=data, calendar_opts=opts.CalendarOpts(range_=['2018-1', '2018-7']))     # range_决定了时间尺度
    .set_global_opts(
        title_opts=opts.TitleOpts(title='Calendar-2018年微信步数'),
        visualmap_opts=opts.VisualMapOpts(
            max_=25000,
            min_=100,
            range_size=[10, 20],         # 不知道干嘛的
            orient='horizontal',
            is_calculable=True,
            is_piecewise=True,     # 颜色条是否分成pieces:True:pices, False:一根长条
            pos_top='230px',
            pos_left='100px',
        ),
    )
)
# calend.render('calendar_echats.html')
page.add(calend)

from pyecharts import options as opts
from pyecharts.globals import SymbolType
words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
    ("Express", 1112),
    ("Home", 865),
    ("Johnny Depp", 847),
    ("Lena Dunham", 582),
    ("Lewis Hamilton", 555),
    ("KXAN", 550),
    ("Mary Ellen Mark", 462),
    ("Farrah Abraham", 366),
    ("Rita Ora", 360),
    ("Serena Williams", 282),
    ("NCAA baseball tournament", 273),
    ("Point Break", 265),
    ]

worldcloud = (
    charts.WordCloud()
    .add("", words, word_size_range=[20, 100], shape='diamond')
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
    )

page.add(worldcloud)


page.render('calendar_bar_echarts.html')
make_snapshot(snapshot, page.render('calendar_bar_echarts.html'), "calendar_bar_echarts.jpeg")
