'''
Created on 2022/09/17

@author: nayuf
'''

class MyClass:
    def __new__(cls):
        print('__new__')
        print(cls)
    
    def __init__(self):
        print('__init__')
    
    def __str__(self):
        return 'test'

class MyStr(str):
    def __new__(cls, text):
        print('__new__')
        return super().__new__(cls, text)
    
    def __init__(self, text):
        print('__init__')
    
    def __str__(self):
        return "***** " + super().__str__()
