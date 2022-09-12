'''
Created on 2022/09/12

@author: nayuf
'''

class Sample:
    # ここに定義するのはクラス変数
    val = []
    
    def __init__(self, x):
        # self.~ はインスタンス変数
        self.x = x

def testClassVariable():
    s1 = Sample(300)
    s2 = Sample(400)
    
    s1.val.append(100)
    s2.val.append(200)
    
    print(Sample.val)
    print(s1.val)
    print(s2.val)
    print(s1.x)
    print(s2.x)