class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h
        
    def area(self)->int:
        return self.width*self.height
    
rect1 = Rectangle(10,20)
print(rect1.area()) 