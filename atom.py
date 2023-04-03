
class Atom():
    
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    
    def __eq__(self, other):
             if self.x == other.x and self.y == other.y:
                  return True
             else:
                  return False
             