class Vehicle :
    def __init__ (self,speed):
        self.speed=speed
        
class Car(Vehicle):
    def __init__(self, speed,brand):
        # super().__init__(speed)
        self.brand=brand
        Vehicle.__init__(self,speed)
        
    def info(self):
        return {"speed":self.speed,"brand":self.brand}

c1= Car(280,"Borsh")

print(c1.info())