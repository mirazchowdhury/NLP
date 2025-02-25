class Animal:
    def __init__(self,name):
        self.n = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.n} speaks gheu gheu"
    
dog = Dog("Buddy")
print(dog.speak())
        