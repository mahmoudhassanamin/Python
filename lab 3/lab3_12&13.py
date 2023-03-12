class Shape :
    def __init__(self,color):
        self.color=color
    
class Rectangle(Shape):
    def __init__(self,color,w,h):
        Shape.__init__(self,color)
        self.width=w
        self.height=h
    def area(self):
        return self.width*self.height
class Circle(Shape) :
    def __init__(self,color,radius):
        Shape.__init__(self,color)
        self.radius=radius
    def area(self):
        return self.radius**2

r1= Rectangle("blue",2,4)
c1=Circle("red",3)

print(f'Rectangle area = {r1.area()} cm')
print(f'Circle area = {c1.area()} cm')