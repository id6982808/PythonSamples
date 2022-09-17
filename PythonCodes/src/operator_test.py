'''
Created on 2022/09/17

@author: nayuf
'''

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        
        return Coordinate(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
    
        return Coordinate(x, y)
    
    def __str__(self):
        return "coordinate:({0},{1})".format(self.x, self.y)
