"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午9:00
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : die_visual.py
"""
from die import  Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die=Die()

# 产生10000个随机点数
results=[]
for roll_num in range(10000):
    result=die.roll()
    results.append(result)
#print(results)

# 统计点数
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 使用plotly进行数据可视化
# Plotly不能直接
# 接受函数range() 的结果,因此需要使用函数list() 将其转换为列表。
x_values=list(range(1,die.num_sides+1))
# Plotly类
# Bar() 表示用于绘制条形图的数据集
data=[Bar(x=x_values,y=frequencies)]

x_axis_config={'title':'result'}
y_axis_config={'title':'frequencies'}
# 类Layout() 返回一个指定图表布局和配置的对象
my_layout=Layout(title='result',xaxis=x_axis_config,yaxis=y_axis_config)
# 为生成图表,我们调用了函数offline.plot() (见❺)。这个函数需要一个包含
# 数据和布局对象的字典,还接受一个文件名,指定要将图表保存到哪里。这里将输
# 出存储到文件d6.html。
offline.plot({'data':data,'layout':my_layout},filename='d6.html')