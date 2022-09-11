'''
Created on 2022/09/11

@author: nayuf
'''

class User(object):
    """
    ユーザクラス
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

def say(user):
    print('私の名前は%sです。%s歳です。'% (user.name, user.age))
