"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午12:44
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : rw_visual.py
"""
import matplotlib.pyplot as plt

from RandomWalk import RandomWalk

rw=RandomWalk(50000)
rw.fill_walk()
plt.style.use('classic')
fig,ax=plt.subplots(figsize=(10,6))
point_numbers=range(rw.num_points)
ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
# 隐藏坐标轴。
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
