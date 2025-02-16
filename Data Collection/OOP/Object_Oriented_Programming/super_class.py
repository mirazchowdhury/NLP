class Parent:
    def __init__(self,name):
        self.name =  name
    def greet(self):
        return f"Hello!I am {self.name}"
    
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)  #calling parents __init__ method
        self.age = age

    def greet(self):
        parent_greeting = super().greet() #calling parents greet method
        return f"{parent_greeting} and I'm {self.age} years old"        

#Example Usage
child = Child("Aliss",28)

print(child.greet())

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello! I am {self.name}"

# class Child(Parent):  # Child class inherits from Parent
#     def __init__(self, name, age):
#         super().__init__(name)  # Calls Parent's __init__ method
#         self.age = age

#     def greet(self):
#         parent_greeting = super().greet()  # Calls Parent's greet method
#         return f"{parent_greeting} and I'm {self.age} years old"

# # Example Usage
# child = Child("Aliss", 28)
# print(child.greet())
