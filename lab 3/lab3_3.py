class Employee :
    def __init__(self,name,age,salary):
        self.__name=name
        self.__age=age
        self.__salary=salary
    
    def setname (self,name):
        self.__name=name  
    def setage (self,age):
        self.__age=age  
    def setsalary (self,salary):
        self.__salary=salary  
    def getname (self):
        return self.__name  
    def getage (self):
        return self.__age  
    def getsalary (self):
        return self.__salary
    def raise_salary(self,percent):
        self.__salary+=((percent/100)*self.__salary)
         

emp1= Employee("mahmoud",27,10000)
emp1.raise_salary(10)
print(f'mahmoud\'s salary : {emp1.getsalary()} E.P')
        