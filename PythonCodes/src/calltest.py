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

def call_10():
    import class_decorator_test as cdt
    
    NewSampleCls = cdt.add_member(cdt.Sample)
    obj = NewSampleCls()
    print(obj.x)
    
    obj2 = cdt.Sample2()
    print(obj2.x)
    
def call_11():
    import special_method_test as smt
    
    user = smt.User("Kuro", 30)
    print(user)
    print(repr(user))
    
    p0 = smt.Coordinate(0, 0)
    p1 = smt.Coordinate(100, 200)
    p2 = smt.Coordinate(0, 200)
    
    if p0:
        print("点p0は真")
    
    if p1:
        print("点p1は真")
    
    if p2:
        print("点p2は真")
        
def call_12():
    import descriptor_test as dt
    
    obj = dt.Sample('test')
    print(obj.descriptor)
    print(obj.x)
    
    obj.descriptor = 'sample2'
    obj.x = 'test2'
    print(obj.descriptor)
    print(obj.x)
    
    del obj.descriptor
    #print(obj.descriptor)
    
    print(obj.y)
    print(dt.Sample.y)

def call_13():
    import new_test as nt
    
    obj = nt.MyClass()
    print(obj)
    
    obj = nt.MyStr('my_str')
    print(obj)

def call_14():
    import operator_test as ot
    
    c1 = ot.Coordinate(1000, 2000)
    c2 = ot.Coordinate(300, 400)
    
    print(c1 + c2)
    print(c1 - c2)

def call_15():
    import exception_test as et
    
    et.test()
    print(et.sample(2))
    print(et.sample('test'))

def call_16():
    import list_test as lt
    
    lt.list_test()

def call_17():
    import map_test as mt
    
    data = mt.apply_map(mt.calc_double, [1, 3, 6, 50, 5])
    print(list(data))
    
    data = mt.apply_map(lambda x : x * 3, [1, 3, 6, 50, 5])
    print(list(data))

def call_18():
    import filter_test as ft
    
    data = ft.filter_test(ft.is_odd, [1, 2, 4, 5, 6, 10, 11])
    print(list(data))
    