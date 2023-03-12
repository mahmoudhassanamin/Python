class Calculator:
    # @staticmethod
    # def add (num1,num2):
    #     return num1+num2
    
    # or
    @classmethod
    def add(cls,num1,num2):
        return num1+num2
    
print(Calculator.add(45,50))