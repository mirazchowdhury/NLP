class Animal:
    
    def speak(self):
        pass 

    #Base class does not provide a specific implementation

class Dog(Animal):
    def speak(self):
        return f"Geo geo"
    
class Cat(Animal):
    def speak(self):
        return f"meu meu"

dog = Dog()
cat = Cat()

print(dog.speak()) 
print(cat.speak())