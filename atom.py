
class Atom():
    
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
    