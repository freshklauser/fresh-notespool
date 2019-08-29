# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-06-21 09:34:22
# @Last Modified by:   klaus
# @Last Modified time: 2019-06-22 11:47:23

from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Page, Pie
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType

''' Notice input data type for different type figure '''

def bar_datazoom_slide():
    c = (
        # Default: width='900px', height='500px'
        Bar()                   # init_opts=opts.InitOpts(width='800px', height='500px')
        .add_xaxis(Faker.days_attrs)
        .add_yaxis('商家A', Faker.days_values)
        #  yaxis_data: Sequence[Numeric, opts.BarItem, dict]
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Bar-DataZoom(slider-水平)'),
            datazoom_opts=[opts.DataZoomOpts()],
        )
    )
    return c

def line_markpoint():
    c = (
        Line()                  # init_opts=opts.InitOpts(width='800px', height='500px')
        .add_xaxis(Faker.choose())
        .add_yaxis(
            '商家A',
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(type_='min')]      # 标记最小值点
                )
            )
        .add_yaxis(
            '商家B',
            Faker.values(),
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(type_='max')]      # 标记最大值点
                )
            )
        .set_global_opts(title_opts=opts.TitleOpts(title='Line-MarkPoint'))
    )
    return c

def pie_rosetype():
    v1 = Faker.choose()
    v2 = Faker.choose()
    while v1 == v2:
        v2 = Faker.choose()
    print(v1, v2)
    c = (
        Pie()                   # init_opts=opts.InitOpts(width='800px', height='500px')
        .add(
            'pie-legend_radius',
            # 系列数据项，格式为 [(key1, value1), (key2, value2)]
            [list(z) for z in zip(v1, Faker.values())],
            color='orange',
            radius=['25%', '60%'],         # 扇区圆心角展现数据的百分比，半径展现数据的大小
            center=['75%', '50%'],         # 饼图的中心（圆心）坐标
            rosetype='radius',             # 有'radius'和'area'两种模式
            label_opts=opts.LabelOpts(is_show=True, position='insideBottomLeft'), # 全局变量中设置legend即可
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .add(
            'pie-legend_area',
            # 系列数据项，格式为 [(key1, value1), (key2, value2)]
            [list(z) for z in zip(v2, Faker.values())],
            color='orange',
            radius=['25%', '60%'],         # 第一项是内半径，第二项是外半径
            center=['25%', '50%'],         # 饼图的中心（圆心）坐标,默认设置成百分比，
                                           # 设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
            rosetype='area',               # 有'radius'和'area'两种模式
            label_opts=opts.LabelOpts(is_show=True, position='insideBottomRight'),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='Pie-rose'),
            legend_opts=opts.LegendOpts(
                type_='scroll',
                is_show=True,
                pos_left='center',
                pos_bottom='bottom')
            )
    )
    return c

def grid_mutil_yaxis():
    x_data = ['{}月'.format(i) for i in range(1, 13)]
    bar = (
        Bar()           # init_opts=opts.InitOpts(width='800px', height='500px')
        .add_xaxis(x_data)
        .add_yaxis(
            '蒸发量',
            [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
            yaxis_index=0,              # 多y轴中不同y轴的索引
            color='#d14a61',
            )
        .add_yaxis(
            '降水量',
            [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
            yaxis_index=1,
            color='#5793f3',
            )
        .extend_axis(                   # 新增y轴配置项，参考global_options.AxisOpts
            yaxis=opts.AxisOpts(
                name='蒸发量',
                type_='value',          # type_ 表示什么？？？  y轴数据类型？？？？
                min_=0,
                max_=250,
                position='right',       # y坐标轴位置
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='#d14a64')
                    ),
                axislabel_opts=opts.LabelOpts(formatter='{value} ml'),
                ),
            )   # formatter 中括号里的什么要求？？？
        .extend_axis(
            yaxis=opts.AxisOpts(
                name='温度',
                type_='value',
                min_=0,
                max_=25,
                position='left',        # 温度y坐标轴在左
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='#675bba')),
                axislabel_opts=opts.LabelOpts(formatter='{value} °C'),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(opacity=1)    # 不透明度？？
                    ),
                )
            )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(
                name='降水量',
                min_=0,
                max_=250,
                position='right',
                offset=80,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='#FF4500')
                    ),
                axislabel_opts=opts.LabelOpts(formatter='{value} ml'),
                ),
            title_opts=opts.TitleOpts('Grid-Multi_Y sample'),
            tooltip_opts=opts.TooltipOpts(is_show=True, trigger='axis', axis_pointer_type='cross'),
            )
        )
    line = (
        # theme参数对子图好像没用
        Line()          # init_opts=opts.InitOpts(width='800px', height='500px')
        .add_xaxis(x_data)
        .add_yaxis(
            '平均温度',
            [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
            yaxis_index=2,
            color="orange",
            )
        )
    bar.overlap(line)
    grid = (
        Grid()
        .add(bar, opts.GridOpts(pos_left='5%', pos_right='20%'), is_control_axis_index=True)
        # .add(line, opts.GridOpts(pos_right='55%'))
        )
    return grid


if __name__ == '__main__':
    # 顺序图表，Page()不设置layout参数
    # page = Page()
    # page.add(bar_datazoom_slide(), line_markpoint(), pie_rosetype(), grid_mutil_yaxis())
    # page.render('multi-figure page.html')
    # 布局图标
    page1 = Page(layout=Page.SimplePageLayout)
    page1.add(bar_datazoom_slide(), line_markpoint(), pie_rosetype(), grid_mutil_yaxis())
    page1.render('multi-figure page_layout.html')
    # make_snapshot(snapshot, page1.render('multi-figure page_layout.html'), 'multi-figure page_layout.png')
    # grid = grid_mutil_yaxis()
    # grid.render()
    # make_snapshot(snapshot, grid.render(), 'adf.jpeg')
