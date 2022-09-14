'''
Created on 2022/09/10

@author: nayuf

呼び出しテスト用の関数
'''

import sys
sys.path.append('.')

def call_01():
    print("call 01")

def call_02():
    print("call 02")

def call_03():
    from user import User
    from user import say

    user1 = User("suzuki", 26)
    user2 = User("sato", 31)
    
    say(user1)
    say(user2)
    
def call_04():
    import coordinate
    
    cood = coordinate.Coordinate()
    cood.x = 100
    cood.y = 200
    cood.show_coordinate()
    
    print(cood)

def call_05():
    import ClassVariableTest as cvt
    
    cvt.testClassVariable()

def call_06():
    import class_and_static_method_test as casmt
    
    casmt.test_class_method()
    casmt.test_static_method()

def call_07():
    import inherit_test as it
    
    obj = it.Sub()
    obj.func1()
    obj.func2()
    
    e = it.Employee("Suzuki", 45, "営業部")
    e.say_name()
    e.say_department()

def call_08():
    import private_member_test as pmt
    
    user = pmt.User("Yamada", 45)
    user.name = "Yoshida"
    user._age = 39
    print(user._age)

def call_09():
    import property_test as pt
    
    obj1 = pt.Sample1()
    print(obj1.get_text())
    obj1.set_text(None)
    obj1.delete_text()
    
    obj2 = pt.Sample2()
    print(obj2.text)
    obj2.text = None
    print(obj2.text)
    del obj2.text
    print(obj2.text)
