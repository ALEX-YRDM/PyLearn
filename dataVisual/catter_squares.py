import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]
x_values=range(1,1001)
y_values=[x**2 for x in x_values]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
# 颜色可以使用rgb如 （0,0.8,0）
# ax.scatter(x_values, y_values,s=10,color='red')

"""
颜色映射 (colormap)是一系列颜色,从起始颜色渐变到结束颜色。

"""
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# plt.show()
# 自动保存图表
# 第一个实参指定要以什么文件名保存图表,这个文件将存储到scatter_squares.py
# 所在的目录。第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围
# 多余的空白区域,只需省略这个实参即可。
plt.savefig('squares_plot.png', bbox_inches='tight')