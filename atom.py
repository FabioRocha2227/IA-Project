import pygame

class atom():
  
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
      
    def set_x(self, value):
        self.x = value
    
    def set_y(self, value):
        self.y = value


