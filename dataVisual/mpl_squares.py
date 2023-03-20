
import matplotlib.pyplot as plt

"""
我们创建了一个名为squares 的列表,在其中存储要用来制作图表的数据。然后,
采取了另一种常见的Matplotlib做法——调用函数subplots() (见❶)。这个函
数可在一张图片中绘制一个或多个图表。变量fig 表示整张图片。变量ax 表示图
片中的各个图表,大多数情况下要使用它
"""
plt.style.use('seaborn-v0_8-darkgrid')
squares = [1,4,9,16,25]
fig,ax=plt.subplots()
"""
接下来调用方法plot() ,它尝试根据给定的数据以有意义的方式绘制图表。函数
plt.show() 打开Matplotlib查看器并显示绘制的图表,如图15-1所示。在查看器
中,你可缩放和导航图形,还可单击磁盘图标将图表保存起来。
"""

"""
参数linewidth (见❶)决定了plot() 绘制的线条粗细。方法set_title()
(见❷)给图表指定标题。在上述代码中,出现多次的参数fontsize 指定图表中
各种文字的大小。
方法set_xlabel() 和set_ylabel() 让你能够为每条轴设置标题(见❸)。方
法tick_params() 设置刻度的样式(见❹),其中指定的实参将影响 轴和 轴
上的刻度(axes='both' ),并将刻度标记的字号设置为14(labelsize=14
)。
"""
input_values=[1,2,3,4,5]
ax.plot(input_values,squares,linewidth=3)
ax.set_title("squares",fontsize=24)
ax.set_xlabel("x",fontsize=24)
ax.set_ylabel("squares",fontsize=24)
ax.tick_params(axis='both',labelsize=14)
plt.show()
"""
plt style
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh',
 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 
 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 
 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook',
  'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 
  'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

"""
#print(plt.style.available)
