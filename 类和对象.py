class animal:
    species="dont know"
    age="1212"
    def __init__(self,name):
        self.name=name
    def speak(self):    
        return f"{self.name} make a sound!"
    @classmethod
    def qqq(cls):
        return cls.species
    @classmethod
    def www(cls):
        return cls.age
class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    def speak(self):
        return f"{self.name}say wangwang"
dog1=dog("xiaowww","金毛品种") 
print(dog1.speak())
print(animal.qqq())
print(animal.www())
class animal:
    def __init__(self,name,age,breed)
        super().__init__(name)
        self.age=age
        self.breed=breed
    class animal:
        def __init__(self,name,age,breed)
            super().__init__
















        
