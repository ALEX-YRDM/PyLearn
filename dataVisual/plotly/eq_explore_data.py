"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/4 下午4:16
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : eq_explore_data.py
"""
# 首先导入模块json ,以便恰当地加载文件中的数据
import json
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
filename='data/eq_data_30_day_m1.json'
# 将其存储到all_eq_data
# 中(见❶)。函数json.load() 将数据转换为Python能够处理的格式,这里是一
# 个庞大的字典
with open(filename) as f:
    all_eq_data=json.load(f)

# 创建一个文件,以便将这些数据以易于阅读的方式写入其
# 中。函数json.dump() 接受一个JSON数据对象和一个文件对象,并将数据写入这
# 个文件中(见❸)。参数indent=4 让dump() 使用与数据结构匹配的缩进量来设
# 置数据的格式。
# readable_file='data/readable_eq_data.json'
# with open(readable_file,'w') as f:
#    json.dump(all_eq_data,f,indent=4)

all_eq_dicts=all_eq_data['features']
# print(len(all_eq_dicts))

# 我们创建了一个空列表,用于存储地震震级,再遍历列表all_eq_dicts(见❶)。每
# 次地震的震级都存储在相应字典的'properties' 部分的'mag' 键下(见❷)。
# 我们依次将地震震级赋给变量mag ,再将这个变量附加到列表mags 末尾
# mags=[]
# for eq_dict in all_eq_dicts:
#     mag=eq_dict['properties']['mag']
#     mags.append(mag)
# print(mags[:10])
mags,titles,lons,lats=[],[],[],[]
for eq_dict in all_eq_dicts:
    mag=eq_dict['properties']['mag']
    title=eq_dict['properties']['title']
    lon=eq_dict['geometry']['coordinates'][0]
    lat=eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data=pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=["经度",'纬度','位置',"震级"]
)
data.head()

fig=px.scatter(
    # x=lons,
    # y=lats,
    data,
    #labels={"x": "经度", "y": "纬度"},
    x="经度",
    y="纬度",
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    size="震级",
    size_max=10,
    color="震级",
    title="全球地震散点图",
    hover_name="位置"
)
# scatter=go.Scattermapbox(lat=lats,lon=lons)
# fig=go.Figure(scatter)

fig.write_html('global_earthquakes.html')
fig.show()