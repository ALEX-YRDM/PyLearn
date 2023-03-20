# Author: Alex Albert
# Date: 2023/1/4 11:22
# Project: variable and simple datatype
import math
import this  # python之禅
message = "hello python"
print(message)

'''
python变量命名规则:
1.变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数
字打头; 与c,c++,java相同
2.变量名不能包含空格，但能使用下划线来分隔其中的单词
3.不要将Python关键字和函数名用作变量名
4.变量名应既简短又具有描述性 见文知义
5.慎用小写字母l 和大写字母O 因为它们可能被人错看成数字1 和0 。

很多编程错误都简单，只是在程序的某一行输错了一个字符。为找出这种错误而花费很
长时间的大有人在。很多程序员天资聪颖、经验丰富，却为找出这种细微的错误花费数
小时。你可能觉得这很好笑，但别忘了，在你的编程生涯中，经常会有同样的遭遇。
'''
# python 字符串,可以单引号也可以双引号
name = "taylor swift"
print(name.title())  # Str.title() 以首字母大写的方式显示每个单词
country = "America"
# info = f"{name} {country}"  python3.6+
# info = format(name+" "+country)
info = name+" "+country
print(info)

# \t 制表符 \n 换行符
# rstrip() 删除字符串末尾多余空白
# lstrip() 删除字符串开头多余空白
# strip() 删除字符串两端多于空白

name = "python   "
print(name.rstrip())

# 整数 + - * /  **乘方
# 浮点数
'''
1.将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除
>>> 4/2
2.0
2.如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
3.书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读：
>>> universe_age = 14_000_000_000  Python 3.6和更高的版本支持。
'''
age = 18_000_000_000
print(age)

# 同时给多个变量赋值
a, b, c = 1, 2, 3
print(a, b, c)

# 常量 constant
MAX_SIZE = 500

# python注释  #

