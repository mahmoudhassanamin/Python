class Animal:
    def __init__(self,name):
        self.name=name

class Pet :
    def __init__(self,owner):
        self.owner=owner

class  Dog(Animal,Pet):
    def __init__(self, name,owner,breed):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
        self.breed=breed
        
    def info (self):
        return {"name":self.name,"owner":self.owner,"breed":self.breed}

dog1=Dog("POGY","mahmoud",("soso","fofo","nono"))

print(dog1.info())     