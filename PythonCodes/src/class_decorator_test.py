'''
Created on 2022/09/15

@author: nayuf
'''

def add_member(cls):
    cls.x = 'sample'
    return cls

class Sample:
    pass

@add_member
class Sample2:
    pass