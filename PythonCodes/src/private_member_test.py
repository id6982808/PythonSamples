'''
Created on 2022/09/14

@author: nayuf
'''
class User:
    def __init__(self, name="", age=0):
        self.name = name # public member
        self._age = age # private member
