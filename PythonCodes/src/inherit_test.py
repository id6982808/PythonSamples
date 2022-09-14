'''
Created on 2022/09/14

@author: nayuf
'''
class Base:
    def func1(self):
        print('func1')

class Sub(Base):
    def func2(self):
        print('func2')

class User:
    """
    ユーザクラス
    """
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    def say_name(self):
        print("私の名前は" + self.name + "です。")

class Employee(User):
    """
    社員クラス
    """
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department
    
    def say_department(self):
        print("私の部署は" + self.department + "です。")
