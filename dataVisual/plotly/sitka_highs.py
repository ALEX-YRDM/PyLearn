"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午9:57
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : sitka_highs.py
"""
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename= 'data/sitka_weather_07-2018_simple.csv'
filename='data/sitka_weather_2018_simple.csv'

# 导入模块csv 后,将要使用的文件的名称赋给filename 。接下来,打开这个文
# 件,并将返回的文件对象赋给f
with open(filename) as f:
    # 调用csv.reader() 并将前面存
    # 储的文件对象作为实参传递给它,从而创建一个与该文件相关联的阅读器对象(见
    # ❷)。这个阅读器对象被赋给了reader 。
    reader=csv.reader(f)
    # 模块csv 包含函数next() ,调用它并传入阅读器对象时,它将返回文件中的下一
    # 行。在上述代码中,只调用了next() 一次,因此得到的是文件的第一行,其中包
    # 含文件头
    header_row=next(reader)
    #  print(header_row) # ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']

    """
    在循环中,对列表调用了enumerate() (见❶)来获取每个元素的索引及其值。
    0 STATION
    1 NAME
    2 DATE
    3 PRCP
    4 TAVG
    5 TMAX
    6 TMIN
    """
    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    # 创建一个名为highs 的空列表
    dates,highs=[],[]
    # 阅读
    # 器对象从其停留的地方继续往下读取CSV文件,每次都自动返回当前所处位置的下一
    # 行。由于已经读取了文件头行,这个循环将从第二行开始——从这行开始包含的是
    # 实际数据。每次执行循环时,都将索引5处(TMAX 列)的数据附加到highs 末尾
    for row in reader:
        # 在文件中,这项数据是以字符串格式存储的,因此在附加到highs 末尾
        # 前,使用函数int() 将其转换为数值格式,以便使用。
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        dates.append(current_date)
        high=int(row[5])
        highs.append(high)
# print(highs)
plt.style.use('classic')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red')

# 调用
# fig.autofmt_xdate() 来绘制倾斜的日期标签,以免其彼此重叠
fig.autofmt_xdate()

ax.tick_params(axis='both',which='major',labelsize=16)
plt.show()

# datatime模块  将字符串日期转换为日期类
"""
from datatime import datatime
first-data=datatime.strptime('2018-07-01','%Y-%m-%d')
print(first_data)  2018-07-01 00:00:00

%A      星期几,如Monday
%B
        月份名,如January
%m
        用数表示的月份(01~12)
%d
        用数表示的月份中的一天(01~31)
%Y
        四位的年份,如2019
%y
        两位的年份,如19
%H
        24小时制的小时数(00~23)
%I
        12小时制的小时数(01~12)
%p
        am或pm
%M
        分钟数(00~59)
%S
        秒数(00~61)
"""