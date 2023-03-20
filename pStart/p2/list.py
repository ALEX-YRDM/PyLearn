# Author: Alex Albert
# Date: 2023/1/4 12:25
# Project: 列表
"""
1.列表 由一系列按特定顺序排列的元素组成。
    可以将任何东西加入列表中，其中的元素之间可以没
    有任何关系。列表通常包含多个元素
2.在Python中，用方括号[]表示列表，并用逗号分隔其中的元素

"""
# 1.列表定义
car = []  # 定义空列表
color = ['red', 'green', 'blue']
print(color)
''' 输出结果如下:
['red', 'green', 'blue']
'''

# 2.列表元素访问: 通过索引
print(color[0], color[1], color[2])
# print(color[3]) IndexError: list index out of range

# python支持负数索引  -1表示最后一个 -2表示倒数第二,以此类推
print(color[-1],color[-2],color[-3])

# 3.修改,添加和删除列表元素

# 3.1修改
color[0] = "yellow"  # 像这样直接修改即可
print(color[0], color[1], color[2])
# 输出结果:yellow green blue

# 3.2添加
# 3.2.1 末尾添加 append()
color.append("purple")
print(color)  # ['yellow', 'green', 'blue', 'purple']

# 3.2.2 随机位置插入 insert()
color.insert(1, "white")
print(color)  # ['yellow', 'white', 'green', 'blue', 'purple']

# 3.3.删除
# 3.3.1 使用del删除
del color[0]
print(color)  # ['white', 'green', 'blue', 'purple']

# 3.3.2 pop() 弹出末尾元素并返回
Acolor = color.pop()
print(Acolor)  # purple
print(color)  # ['white', 'green', 'blue']

# 3.3.3 pop(index) 弹出指定位置元素并返回
Acolor = color.pop(0)
print(Acolor)  # white
print(color)  # ['green', 'blue']

# 3.3.4 根据值删除元素 remove()
color.remove("green")
print(color)  # ['blue']

# 4.组织列表
# 4.1 列表排序 sort() 会对列表本身作出改变
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 默认升序
# cars.sort()
# print(cars)  ['audi', 'bmw', 'subaru', 'toyota']

# 降序
# cars.sort(reverse=True)
# print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

# 4.2 使用sorted() 可以显示排序,但不改变原列表
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']

# 4.3 逆序排列列表 reverse()
cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']

# 4.4 获得列表长度 len()
print(len(cars))  # 4

