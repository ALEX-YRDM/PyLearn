"""
# -*- coding: utf-8 -*-
# @Time    : 2023/3/3 下午8:58
# @Author  : pissenlit
# @Email   : yirendm202022@gmail.com
# @File    : die.py
"""
from random import randint


class Die:
    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        """返回一个1-nums_sides的值"""
        return randint(1,self.num_sides)
