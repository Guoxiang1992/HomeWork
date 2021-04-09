# -*- coding: utf-8 -*- 
# @File : Class_Animal.py
"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.color = "灰色"
        self.age = age
        self.gender = "雌性"
    def shout(self):
        print(f"{self.name}今年{self.age}岁了,颜色:{self.color},性别:{self.gender},生气了会叫!")
    def run(self):
        print(f"{self.name}今年{self.age}岁了,颜色:{self.color},性别:{self.gender},吃饱了就会到处跑!")

if __name__ == '__main__':
    animal = Animal("阿黄",3)
    animal.shout()
    animal.run()

