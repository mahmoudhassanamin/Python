class Car :
    # make, model, year, and mileage
    def __init__(self,make,model,year,mileage) :
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
        
    def drive(self,mile):
        self.mileage+=mile

car1 = Car("egypt","hatchback",2025,0)
car1.drive(2)
print(car1.mileage)
car1.drive(2)
print(car1.mileage)
        