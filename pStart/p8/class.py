# Author: Alex Albert
# Date: 2023/1/9 14:26
# Project:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is sitting")

    def roll(self):
        print(self.name.title()+" rolled over")


alex = Dog("willie", 6)
alex.sit()
