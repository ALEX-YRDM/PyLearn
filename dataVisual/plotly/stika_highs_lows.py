"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午10:26
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : stika_highs_lows.py
"""
import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename='data/sitka_weather_2018_simple.csv'
# 类似游标 初始时指向第一行上面，所以需要next
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)

    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(current_date)
        high=int(row[5])
        highs.append(high)
        low=int(row[6])
        lows.append(low)

plt.style.use('classic')
fig,ax=plt.subplots()
# 实参alpha 指定颜色的透明度。alpha 值为0表示完全透明,为1(默认设
# 置)表示完全不透明。通过将alpha 设置为0.5,可让红色和蓝色折线的颜色看起
# 来更浅。
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)

# 向fill_between() 传递一个 值系列(列表dates ),以及两个 值
# 系列(highs 和lows )。实参facecolor指定填充区域的颜色,还将alpha 设置
# 成了较小的值0.1,让填充区域将两个数据系列连接起来的同时不分散观察者的注意
# 力。
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
fig.autofmt_xdate()
plt.show()