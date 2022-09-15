'''
Created on 2022/09/15

@author: nayuf
'''

class MyDescriptor:
    def __init__(self, text):
        self.text = text
    
    def __get__(self, instance, owner):
        return "* " + self.text
    
    def __set__(self, instance, text):
        self.text = text + "!"
    
    def __delete__(self, instance):
        del self.text
        print('text属性が削除されました')

class Sample:
    descriptor = MyDescriptor('sample')
