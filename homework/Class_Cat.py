# -*- coding: utf-8 -*- 
# @File : Class_Cat.py
from Class_Animal import Animal
class Cat(Animal):
    def __init__(self,name,age,):
        self.hair = "短毛"
        super().__init__(name,age)
    def capacity(self):
        print(f"{self.name}今年{self.age}岁了,{self.hair},颜色:{self.color},性别:{self.gender},会抓老鼠")
    def shout(self):
        print(f"{self.name}今年{self.age}岁了,{self.hair},颜色:{self.color},性别:{self.gender},饿了会”喵喵”叫!")
if __name__ == '__main__':
    cat = Cat("小咪",2)
    cat.capacity()
    cat.shout()
