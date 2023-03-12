class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __del__(self):
        print("in destructor")
        
p1=Person("mahmoud",27)
