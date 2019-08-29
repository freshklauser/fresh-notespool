# -*- coding: utf-8 -*-
# @Author: klaus
# @Date:   2019-06-13 13:57:59
# @Last Modified by:   Klaus
# @Last Modified time: 2019-07-20 23:24:53

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import mpl_toolkits.axisartist as axisartist
# from matplotlib.font_manager import FontProperties
# font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
plt.rcParams['font.sans-serif'] = ['SimHei']      # 用来正常显示中文标签


def lagrangeInterp(x, y, x_interp):
    func = interpolate.lagrange(x, y)
    y_interp = func(x_interp)
    return y_interp


# 疲劳曲线
x1 = np.arange(1, 21, 1)
x2 = np.array([1, 2, 3, 4, 5, 6, 7, 7.5, 7.7, 8, 8.2, 8.5, 9, 9.5, 10])
y1 = np.array([1.0, 1.025, 1.05, 1.09, 1.2, 1.25, 1.3, 1.4,
               2.1, 2.5, 3, 4.2, 5.3, 8, 12, 16, 21, 30, 50, 68])
y2 = np.array([1.04, 1.05, 1.1, 1.3, 1.7, 2.2, 2.9,
               3.4, 4, 4.8, 5.6, 6.8, 8, 14, 18])
# 初始点多项式拟合
poly1 = np.polyfit(x1, y1, deg=6)
y1_poly = np.polyval(poly1, x1)
# 拟合后的点进行插值：拉格朗日插值
x1_interp = np.linspace(1, 21, 201)
y1_interp = lagrangeInterp(x1, y1_poly, x1_interp)
# 初始点多项式拟合
poly2 = np.polyfit(x2, y2, deg=5)
y2_poly = np.polyval(poly2, x2)
# 拟合后的点进行插值：拉格朗日插值
x2_interp = np.linspace(1, 13, 201)
y2_interp = lagrangeInterp(x2, y2_poly, x2_interp) * 0.9
# print(y1_interp[0] - y2_interp[0])

fig = plt.figure(figsize=(10, 8))
# 设置坐标轴 带箭头
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
# 将绘图区对象添加到画布中
fig.add_axes(ax)
# 通过set_axisline_style方法设置绘图区的底部及左侧坐标轴样式
# "-|>"代表实心箭头："->"代表空心箭头
ax.axis['bottom'].set_axisline_style("->", size=1.5)
ax.axis["left"].set_axisline_style("->", size=1.5)
# 通过set_visible方法设置绘图区的顶部及右侧坐标轴隐藏
ax.axis['top'].set_visible(False)
ax.axis['right'].set_visible(False)
# 设置坐标轴标签(貌似没起作用)
# ax1 = plt.gca()                         # 与上文中的ax不一样
ax.set_xlabel('时间', position=(1, None), fontsize=19)
ax.set_ylabel('累计损伤', position=(None, 0.2), fontsize=14)
# 画图
plt.plot(x1_interp, y1_interp, 'forestgreen')       # 使用健康管理系统后的
plt.plot(x2_interp, y2_interp, 'blue')
# 阈值设置
plt.hlines(y1_interp[-1] * 0.96, 1, 23, 'r', linestyles='--')
# 灾难性破坏点, 损伤点
plt.scatter(x1_interp[-2], y1_interp[-2], c='purple', edgecolors='gold', s=60)
plt.scatter(x2_interp[-2], y2_interp[-2], c='purple', edgecolors='gold', s=60)
plt.scatter(x1_interp[40], y1_interp[40], c='red', edgecolors='gold', s=60)
plt.scatter(x1_interp[55], y1_interp[55], c='red', edgecolors='gold', s=60)
# 设置垂直于x轴的线
plt.vlines(x1_interp[55], y1_interp[55],
           y1_interp[-1], linestyles='--', alpha=0.3)
# plt.
# 注释
plt.annotate(
    '{}'.format('灾难性破坏'),
    xy=(x1_interp[-2], y1_interp[-2]),
    xycoords='data',
    xytext=(-20, 12),
    textcoords='offset points',
    fontsize=12
)
plt.annotate(
    '{}'.format('灾难性破坏'),
    xy=(x2_interp[-2], y2_interp[-2]),
    xycoords='data',
    xytext=(-20, 12),
    textcoords='offset points',
    fontsize=12
)
plt.annotate(
    '{}'.format('阈 值'),
    xy=(x1_interp[2], y1_interp[-1]),
    xycoords='data',
    xytext=(10, 0),
    textcoords='offset points',
    fontsize=15,
    color='red'         # 设置字体颜色
)
plt.annotate(
    '{}'.format('阈 值'),
    xy=(x1_interp[2], y1_interp[-1]),
    xycoords='data',
    xytext=(10, 0),
    textcoords='offset points',
    fontsize=15,
    color='red'         # 设置字体颜色
)
plt.annotate(
    '开始损伤',      # 文本内容 , 可格式化方式
    xy=(x1_interp[40], y1_interp[40]),
    xycoords='data',
    xytext=(-50, 20),
    textcoords='offset points',
    fontsize=12,
    color='black',         # 设置字体颜色
    arrowprops=dict(arrowstyle='->',          # 箭头样式， '-|>' '->'
                    connectionstyle='arc3, rad=.2',
                    color='red')         # 箭头属性
)
plt.annotate(
    '检测到损伤',      # 文本内容 , 可格式化方式
    xy=(x1_interp[55], y1_interp[55]),
    xycoords='data',
    xytext=(-60, 40),
    textcoords='offset points',
    fontsize=12,
    color='black',         # 设置字体颜色
    arrowprops=dict(arrowstyle='->',          # 箭头样式， '-|>' '->'
                    connectionstyle='arc3, rad=.0',
                    color='black')         # 箭头属性
)
# 备注文本
plt.text(x1_interp[188], y1_interp[188],
         'B ',         # 文本内容 , 可格式化方式
         fontsize=12,
         ha='right',            # ('center', 'right', 'left')
         # ('top', 'bottom', 'center', 'baseline')
         va='baseline',
         alpha=0.8,
         color='black'
         )
plt.text(x2_interp[187], y2_interp[187],
         'A ',         # 文本内容 , 可格式化方式
         fontsize=12,
         ha='right',            # ('center', 'right', 'left')
         # ('top', 'bottom', 'center', 'baseline')
         va='baseline',
         alpha=0.8,
         color='black'
         )

plt.xlim((1, 23))
plt.xticks(())      # plt.xticks(rotation=90)
plt.yticks(())
# plt.legend()
plt.savefig(r'C:\Users\junkk\OneDrive\handbook\典型轴承疲劳曲线.jpg', dpi=300)
plt.show()
