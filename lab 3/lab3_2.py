import math
class Circle :
    def __init__(self,r):
        self.redius = r
        
    def circumference (self):
        return 2*math.pi*self.redius
    
circle1= Circle(2)
print(circle1.circumference())
    