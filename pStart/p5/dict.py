# Author: Alex Albert
# Date: 2023/1/9 11:49
# Project: ch6 字典

# 字典是一对键-值对,与键关联的值可以为任意python对象
# 1.字典定义:
alien = {
    'color': 'yellow',
    'points': 5
}

# 2.访问字典中的值
print(alien['color'])

# 3.添加键值对
print(alien)  # {'color': 'yellow', 'points': 5}
alien['x_position'] = 0
alien['y_position'] = 200
print(alien)  # {'color': 'yellow', 'points': 5, 'x_position': 0, 'y_position': 200}

# 4.修改字典中的值
alien['x_position'] = 100  # 这样即可

# 5.删除键值对
del alien['color']
print(alien)  # {'points': 5, 'x_position': 100, 'y_position': 200}

# 6.遍历字典
# items()方法返回一个键值对列表
# 6.1遍历键值对
for key, value in alien.items():
    print("key: "+key)
    print("value: "+str(value))

# 6.2 遍历所有键
for key in alien.keys():
    print(key)

# 6.3 遍历所有值
for value in alien.values():
    print(value)



