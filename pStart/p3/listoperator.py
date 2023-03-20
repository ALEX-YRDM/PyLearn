# Author: Alex Albert
# Date: 2023/1/4 13:09
# Project: 操作列表

# 1.遍历整个列表
names = ['alex', 'zbq', 'taylor', 'monica']
for a in names:
    print(a)
    print(a.title())
"""
alex
Alex
zbq
Zbq
taylor
Taylor
monica
Monica
"""
# 2.缩进
"""
Python根据缩进来判断代码行与前一个代码行的关系
"""

# 3.创建数值列表
# 3.1函数 range(start,end) [start,end)
for value in range(1, 5):
    print(value)
"""
1
2
3
4
"""
# 3.2创建数字列表
nums = list(range(1, 10))
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(start,end,step) 指定步长
nums = list(range(1, 10, 2))
print(nums)  # [1, 3, 5, 7, 9]

# 3.3对列表进行简单的统计运算
print(min(nums), max(nums), sum(nums))  # 1 9 25

# 3.4列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

newsquares = [value**2 for value in range(1, 11)]
print(newsquares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 4.使用列表的一部分
# 4.1切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # ['charles', 'martina', 'michael']    [0,3) 左闭右开

print(players[2:4])  # ['michael', 'florence']  [2,4)

print(players[:4])  # [0,4)  start未指定从0开始
print(players[2:])  # 未指定end则遍历后续所有

print(players[-3:])  # 遍历倒数第三到最后一个

# 4.2 对切片的遍历
for i in players[:3]:
    print(i.title())
"""
Charles
Martina
Michael
"""

# 4.3 列表复制
# 依旧拿上面players
new_players = players[:]  # 将players中的所有元素拷贝到new_players
print('old_players:')
print(players)
print('new players: ')
print(new_players)
players.append('hello')
new_players.append('world')
print('old_players:')
print(players)  # ['charles', 'martina', 'michael', 'florence', 'eli', 'hello']
print('new players: ')
print(new_players)  # ['charles', 'martina', 'michael', 'florence', 'eli', 'world']
# 确实为两个列表
# 如果直接赋值,则会将两个变量指向同一个列表
testPlayers = players  # 类似这样会将testPlayers和players指向同一个列表,对任何一个操作都会同步更新

# 5.元组
# 5.1定义: 不可变的列表称为元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 300  TypeError: 'tuple' object does not support item assignment
# 5.2 元组遍历
# 同列表


# 5.3 元组
# 元组元素不可修改,但可将元组变量指向另外一个元组
dimensions = (400, 100)