class Person :
    def __init__(self,name):
        self.name=name
    
class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    
    def info(self):
        return (self.name,self.salary,self.department)

manager1 = Manager("mahmoud",10000,"R&D")

print(manager1.info())