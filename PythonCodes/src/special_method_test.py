'''
Created on 2022/09/15

@author: nayuf
'''

class User():
    """
    ユーザクラス
    """
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is " + self.name)
    
    def __str__(self):
        return "User:" + self.name
    
    def __repr__(self):
        return str({"name": self.name, "age": str(self.age)})

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __bool__(self):
        if self.x or self.y:
            return True
        else:
            return False
