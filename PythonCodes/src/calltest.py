'''
Created on 2022/09/10

@author: nayuf

呼び出しテスト用の関数
'''

import sys
sys.path.append('.')

from user import User
from user import say
import coordinate
import ClassVariableTest as cvt
import class_and_static_method_test as casmt

def call_01():
    print("call 01")

def call_02():
    print("call 02")

def call_03():
    user1 = User("suzuki", 26)
    user2 = User("sato", 31)
    
    say(user1)
    say(user2)
    
def call_04():
    cood = coordinate.Coordinate()
    cood.x = 100
    cood.y = 200
    cood.show_coordinate()
    
    print(cood)

def call_05():
    cvt.testClassVariable()

def call_06():
    casmt.test_class_method()
    casmt.test_static_method()
