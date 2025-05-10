class Polygon:
    def __init__(self, a,b):
        self.a = a
        self.b = b
class Rectangle(Polygon):
    def sq(self):
        print(self.a*self.b)
sq = Rectangle(2,3)