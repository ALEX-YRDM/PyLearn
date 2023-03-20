"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午12:12
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : test.py
"""
import matplotlib.pyplot as plt

x_values=range(1,5001)
y_values=[x*x*x for x in x_values]
fig,ax=plt.subplots()
plt.style.use('seaborn-v0_8-darkgrid')
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.pink,s=10)
plt.savefig('1.png',bbox_inches='tight')

