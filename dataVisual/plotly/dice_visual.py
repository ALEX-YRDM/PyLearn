"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午9:25
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : dice_visual.py
"""

from die import  Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die1=Die(8)
die2=Die(10) # 10面
results=[]
for roll_num in range(9000000): # 9000000还能接受
    result=die1.roll()+die2.roll()
    results.append(result)

frequencies=[]
max_result=die1.num_sides+die2.num_sides

for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)

x_values=list(range(2,max_result+1))
# Plotly类
# Bar() 表示用于绘制条形图的数据集
data=[Bar(x=x_values,y=frequencies)]

# 创建图表时,在字典x_axis_config 中使用了dtick 键(见❹)。这项设置指定
# 了 轴显示的刻度间距。这里绘制的直方图包含的条形更多,Plotly默认只显示某
# 些刻度值,而设置'dtick': 1 让Plotly显示每个刻度值。
x_axis_config={'title':'result','dtick':1}
y_axis_config={'title':'frequencies'}

# 类Layout() 返回一个指定图表布局和配置的对象
my_layout=Layout(title='result',xaxis=x_axis_config,yaxis=y_axis_config)

# 为生成图表,我们调用了函数offline.plot() (见❺)。这个函数需要一个包含
# 数据和布局对象的字典,还接受一个文件名,指定要将图表保存到哪里。这里将输
# 出存储到文件d6.html。
offline.plot({'data':data,'layout':my_layout},filename='d6_d6.html')