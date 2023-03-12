from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
	    pass

class Dog(Animal):
    def speak(self):
         print("Dog sound")
         

class Cat(Animal):
    def speak(self):
         print("Cat sound")

dog1=Dog()
cat1=Cat()
dog1.speak()
cat1.speak()
