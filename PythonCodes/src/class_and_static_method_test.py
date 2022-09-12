'''
Created on 2022/09/12

@author: nayuf
'''

import math

class Coordinate:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show_coordinate(self):
        print(self.x, self.y)
    
    @classmethod
    def create_origin(cls):
        origin = cls(0, 0)
        return origin
    
    @staticmethod
    def calc_dist(cood1, cood2):
        x = cood1.x - cood2.x
        y = cood1.y - cood2.y
        return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))

def test_class_method():
    cood = Coordinate.create_origin()
    cood.show_coordinate()

def test_static_method():
    cood1 = Coordinate(0, 0)
    cood1.x, cood1.y = 100, 100
    
    cood2 = Coordinate(200, 200)
    
    dist = Coordinate.calc_dist(cood1, cood2)
    print(dist)
